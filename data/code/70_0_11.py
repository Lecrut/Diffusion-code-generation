def read_and_print_first_last(file_path):
    try:
        with open(file_path, 'r') as file:
            items = file.read().splitlines()
            if items:
                print(items[0])
                if len(items) > 1:
                    print(items[-1])
            else:
                print("File is empty")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == '__main__':
    read_and_print_first_last('sample.txt')