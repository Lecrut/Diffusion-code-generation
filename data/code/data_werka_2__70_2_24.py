def get_ends(iterable):
    try:
        items = [item for item in iterable]
    except TypeError:
        raise ValueError("input is not iterable")
    if len(items) == 0:
        raise ValueError("iterable is empty")
    return (items[0], items[-1])

if __name__ == '__main__':
    print(get_ends([1, 2, 3, 4, 5]))
    try:
        print(get_ends([]))
    except ValueError as e:
        print(e)
    print(get_ends("python"))