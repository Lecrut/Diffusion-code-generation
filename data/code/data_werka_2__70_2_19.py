def get_first_last(iterable):
    sentinel = object()
    first = sentinel
    last = sentinel
    for item in iterable:
        if first is sentinel:
            first = item
        last = item
    if first is sentinel:
        raise ValueError("iterable is empty")
    return (first, last)

if __name__ == '__main__':
    print(get_first_last([10, 20, 30, 40, 50]))
    try:
        print(get_first_last(()))
    except ValueError as e:
        print(e)
    print(get_first_last([42]))