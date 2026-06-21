def get_ends(iterable):
    it = iter(iterable)
    try:
        first = next(it)
    except StopIteration:
        raise ValueError("iterable is empty")
    last = first
    for item in it:
        last = item
    return (first, last)

if __name__ == '__main__':
    print(get_ends([1, 2, 3, 4, 5]))
    try:
        print(get_ends([]))
    except ValueError as e:
        print(e)
    print(get_ends([42]))
    print(get_ends("python"))