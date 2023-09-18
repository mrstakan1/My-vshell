import os
import tarfile
import zipfile

# Функция для извлечения виртуальной файловой системы из файла формата tar
def extract_tar_virtual_fs(file_path):
    with tarfile.open(file_path, 'r') as tar:
        tar.extractall()
    print(f"Virtual filesystem extracted from {file_path}")

# Функция для извлечения виртуальной файловой системы из файла формата zip
def extract_zip_virtual_fs(file_path):
    with zipfile.ZipFile(file_path, 'r') as zip:
        zip.extractall()
    print(f"Virtual filesystem extracted from {file_path}")

# Функция для получения текущего рабочего каталога
def pwd():
    print(os.getcwd())

# Функция для отображения содержимого текущего каталога
def ls():
    files = os.listdir()
    for file in files:
        print(file)

# Функция для изменения текущего рабочего каталога
def cd(directory):
    try:
        os.chdir(directory)
    except FileNotFoundError:
        print(f"Directory '{directory}' not found")
    except NotADirectoryError:
        print(f"'{directory}' is not a directory")
    except PermissionError:
        print(f"Permission denied for '{directory}'")

# Функция для отображения содержимого файла
def cat(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File '{file_path}' not found")
    except IsADirectoryError:
        print(f"'{file_path}' is a directory")
    except PermissionError:
        print(f"Permission denied for '{file_path}'")

# Основной цикл vshell
def vshell():
    command = ''
    while command != 'exit':
        command = input('$ ')
        if command == 'pwd':
            pwd()
        elif command == 'ls':
            ls()
        elif command.startswith('cd'):
            directory = command.split(' ', 1)[-1]
            cd(directory)
        elif command.startswith('cat'):
            file_path = command.split(' ', 1)[-1]
            cat(file_path)
        elif command == 'exit':
            print("Exiting vshell...")
        else:
            print(f"Command not found: {command}")

# Пример использования vshell
if __name__ == "__main__":
    # virtual_fs_file = 'virtual_fs.tar'  # Путь к файлу с виртуальной файловой системой (tar/zip)
    # file_extension = os.path.splitext(virtual_fs_file)[1]

    # if file_extension == '.tar':
    #     extract_tar_virtual_fs(virtual_fs_file)
    # elif file_extension == '.zip':
    #     extract_zip_virtual_fs(virtual_fs_file)
    # else:
    #     print("Unsupported file format")

    vshell()