def number_range_generator(start, end):
    if start > end:
        start, end = end, start
    for num in range(start, end + 1):
        yield num

if __name__ == '__main__':
    gen = number_range_generator(5, 1)
    print(list(gen))