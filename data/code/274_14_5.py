def print_items(item_list):
    if not isinstance(item_list, list) or not all(isinstance(item, str) for item in item_list):
        raise ValueError("Input must be a list of strings")
    
    for item in item_list:
        print(item)

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    print_items(sample_items)