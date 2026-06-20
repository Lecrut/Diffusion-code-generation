def read_and_print_items(filename):
    try:
        with open(filename, 'r') as file:
            items = file.readlines()
            if items:
                print(items[0].strip())
                print(items[-1].strip())
            else:
                print("File is empty")
    except FileNotFoundError:
        print(f"File {filename} not found")

if __name__ == '__main__':
    read_and_print_items('sample.txt')