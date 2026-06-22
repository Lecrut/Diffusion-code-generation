def range_generator(start, end):
    if start > end:
        start, end = end, start
    for i in range(start, end + 1):
        yield i

if __name__ == '__main__':
    for num in range_generator(5, 10):
        print(num)