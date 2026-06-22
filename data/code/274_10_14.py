def print_items(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    for item in lst:
        print(item)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    try:
        print_items(sample_list)
    except ValueError as e:
        print(e)