def print_first_last(items):
    if not isinstance(items, list) or not all(isinstance(item, int) for item in items):
        raise ValueError("Input must be a list of integers")
    try:
        first = items[0]
        last = items[-1]
        print(first, last)
    except IndexError:
        print("List is empty")

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print_first_last(sample_list)