def first_last(iterable):
    try:
        return next(iter(iterable)), iterable[-1]
    except (StopIteration, IndexError):
        return None, None

if __name__ == '__main__':
    print(first_last([1, 2, 3]))
    print(first_last('hello'))
    print(first_last([]))