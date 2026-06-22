def reverse_range(start, stop=None):
    if stop is None:
        start, stop = 0, start
    for i in range(stop - 1, start - 1, -1):
        yield i

if __name__ == '__main__':
    for item in reverse_range(5):
        print(item)