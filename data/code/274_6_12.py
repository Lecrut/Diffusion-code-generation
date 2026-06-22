def print_items_with_index(items):
    if not isinstance(items, list):
        raise ValueError("Input must be a list")
    
    for index, item in enumerate(items):
        print(f"{index}: {item}")

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    try:
        print_items_with_index(sample_list)
    except ValueError as e:
        print(e)