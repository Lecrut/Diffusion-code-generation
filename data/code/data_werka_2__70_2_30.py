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
    result1 = get_first_last([10, 20, 30, 40])
    print(result1)
    try:
        get_first_last([])
    except ValueError as e:
        print(e)
    result2 = get_first_last("hello")
    print(result2)