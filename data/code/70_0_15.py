def read_first_and_last_items(file_content):
    items = file_content.splitlines()
    if not items:
        return None, None
    first_item = items[0]
    last_item = items[-1]
    return first_item, last_item

if __name__ == '__main__':
    sample_file_content = """apple
banana
cherry
date
elderberry"""
    first, last = read_first_and_last_items(sample_file_content)
    print(first)
    print(last)