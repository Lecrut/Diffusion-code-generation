def print_first_last(items):
    if not isinstance(items, list) or not all(isinstance(x, int) for x in items):
        raise ValueError("Input must be a list of integers")
    if len(items) >= 2:
        print(items[0], items[-1])
    elif len(items) == 1:
        print(items[0])
    else:
        print("List is empty")

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    try:
        print_first_last(sample_list)
    except ValueError as e:
        print(e)