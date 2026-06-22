def get_first_last(seq):
    if hasattr(seq, '__len__'):
        n = len(seq)
        if n == 0:
            raise ValueError("iterable is empty")
        return (seq[0], seq[-1])
    it = iter(seq)
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
    print(get_first_last("hello"))
    try:
        print(get_first_last(42))
    except ValueError as e:
        print(e)