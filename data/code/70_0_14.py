def read_and_print_items(file_path):
    with open(file_path, 'r') as file:
        items = file.readlines()
    
    if items:
        print(items[0].strip())
        print(items[-1].strip())

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    read_and_print_items(sample_file_path)