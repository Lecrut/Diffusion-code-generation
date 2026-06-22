def get_first_last(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")
    last = first
    for item in iterator:
        last = item
    return (first, last)

if __name__ == '__main__':
    print(get_first_last([1, 2, 3, 4, 5]))
    try:
        print(get_first_last([]))
    except ValueError as e:
        print(e)