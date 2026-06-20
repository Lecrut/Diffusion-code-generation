def read_and_print_first_last(file_path):
    try:
        with open(file_path, 'r') as file:
            items = file.readlines()
            if not items:
                print("The file is empty.")
            else:
                first_item = items[0].strip()
                last_item = items[-1].strip()
                print(f"First item: {first_item}")
                print(f"Last item: {last_item}")
    except FileNotFoundError:
        print("File not found.")

if __name__ == '__main__':
    read_and_print_first_last('sample.txt')