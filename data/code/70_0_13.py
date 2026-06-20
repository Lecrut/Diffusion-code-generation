def read_and_print_first_last(file_path):
    try:
        with open(file_path, 'r') as file:
            items = file.read().splitlines()
            if len(items) > 0:
                print(items[0])
                print(items[-1])
            else:
                print("The file is empty.")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")

if __name__ == '__main__':
    read_and_print_first_last('sample.txt')