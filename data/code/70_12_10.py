def get_first_and_last(lst):
    if not lst:
        raise ValueError("List must not be empty")
    return lst[0], lst[-1]

if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]
    first, last = get_first_and_last(numbers)
    print(first, last)