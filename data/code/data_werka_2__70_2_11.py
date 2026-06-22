def get_first_last(iterable):
    it = iter(iterable)
    try:
        first = next(it)
        last = first
        for last in it:
            last = last
        return (first, last)
    except StopIteration:
        raise ValueError("iterable is empty")

if __name__ == '__main__':
    print(get_first_last([1, 2, 3, 4, 5]))
    try:
        print(get_first_last([]))
    except ValueError as e:
        print(e)