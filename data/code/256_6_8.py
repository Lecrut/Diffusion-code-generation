def range_generator(start, end):
    if start > end:
        start, end = end, start
    return (i for i in range(start, end + 1))

if __name__ == '__main__':
    print(list(range_generator(5, 10)))
    print(list(range_generator(10, 5)))