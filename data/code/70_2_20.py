def get_first_last(iterable):
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
    print(get_first_last([10, 20, 30, 40]))
    try:
        print(get_first_last([]))
    except ValueError as e:
        print(e)