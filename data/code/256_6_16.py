def range_generator(start, end):
    if start > end:
        start, end = end, start
    while start <= end:
        yield start
        start += 1

if __name__ == '__main__':
    for num in range_generator(5, 10):
        print(num)