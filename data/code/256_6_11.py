def number_range_generator(start, end):
    if start > end:
        start, end = end, start
    while start <= end:
        yield start
        start += 1

if __name__ == '__main__':
    gen = number_range_generator(5, 10)
    for num in gen:
        print(num)