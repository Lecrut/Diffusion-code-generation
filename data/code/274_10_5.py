def print_items(item_list):
    if not isinstance(item_list, list):
        raise ValueError("Input must be a list")
    for item in item_list:
        print(item)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    try:
        print_items(sample_list)
    except ValueError as e:
        print(e)