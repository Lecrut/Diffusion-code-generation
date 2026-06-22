def get_first_last(iterable):
    try:
        items = list(iterable)
    except TypeError:
        raise ValueError("input is not iterable")
    if not items:
        raise ValueError("iterable is empty")
    return (items[0], items[-1])

if __name__ == '__main__':
    print(get_first_last([1, 2, 3, 4, 5]))
    try:
        print(get_first_last([]))
    except ValueError as e:
        print(e)
    print(get_first_last("python"))