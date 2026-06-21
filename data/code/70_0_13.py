def read_and_print_first_last_items(file_content):
    items = file_content.splitlines()
    if items:
        print(items[0])
        print(items[-1])

if __name__ == '__main__':
    sample_file_content = """apple
banana
cherry
date
elderberry"""
    read_and_print_first_last_items(sample_file_content)