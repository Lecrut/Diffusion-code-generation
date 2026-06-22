def reverse_range(start, stop=None, step=-1):
    if stop is None:
        start, stop = 0, start
    for i in range(stop - 1, start - 1, step):
        yield i

if __name__ == '__main__':
    print(list(reverse_range(5)))
    print(list(reverse_range(10, 2)))
    print(list(reverse_range(3, 8, 2)))