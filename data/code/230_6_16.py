def reverse_range_generator(start, stop=None):
    if stop is None:
        start, stop = 0, start
    while start > stop - 1:
        yield start
        start -= 1

if __name__ == '__main__':
    for item in reverse_range_generator(5):
        print(item)