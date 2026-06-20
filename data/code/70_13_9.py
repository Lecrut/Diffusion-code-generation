def print_first_last(items):
    if not isinstance(items, list):
        raise ValueError("Input must be a list")
    if len(items) == 0:
        raise IndexError("List is empty")
    print(items[0], items[-1])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    try:
        print_first_last(sample_list)
    except Exception as e:
        print(e)