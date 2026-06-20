def print_first_last(items):
    if not items:
        raise ValueError("List is empty")
    first = items[0]
    last = items[-1] if len(items) > 1 else None
    print(first, last)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    try:
        print_first_last(sample_list)
    except ValueError as e:
        print(e)