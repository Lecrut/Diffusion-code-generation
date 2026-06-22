def reverse_range_generator(start, stop=None):
    if stop is None:
        start, stop = 0, start
    for i in range(stop - 1, start - 1, -1):
        yield i

if __name__ == '__main__':
    for num in reverse_range_generator(5, 0):
        print(num)