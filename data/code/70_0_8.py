def read_and_print_first_last(file_path):
    try:
        with open(file_path, 'r') as file:
            items = file.readlines()
            if items:
                print(items[0].strip())
                print(items[-1].strip())
            else:
                print("File is empty")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    read_and_print_first_last('sample.txt')