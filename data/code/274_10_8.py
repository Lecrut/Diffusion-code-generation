ITEM_SEPARATOR = '\n'

def print_list_items(item_list):
    print(ITEM_SEPARATOR.join(item_list))

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    print_list_items(sample_list)