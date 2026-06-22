ITEM_SEPARATOR = ' | '

def print_list(items):
    for item in items:
        print(item, end=ITEM_SEPARATOR)
    print()
if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    print_list(sample_items)