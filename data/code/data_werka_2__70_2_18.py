def get_first_last(iterable):
    try:
        iterator = iter(iterable)
        first = next(iterator)
        last = first
        for last in iterator:
            last = last
        return (first, last)
    except StopIteration:
        raise ValueError("iterable is empty")
    except TypeError:
        raise ValueError("input is not iterable")

if __name__ == '__main__':
    print(get_first_last([1, 2, 3, 4, 5]))
    try:
        print(get_first_last([]))
    except ValueError as e:
        print(e)
    print(get_first_last("python"))