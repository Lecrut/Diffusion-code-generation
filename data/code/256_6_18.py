def generate_range(start, end):
    if start > end:
        start, end = end, start
    for num in range(start, end + 1):
        yield num

if __name__ == '__main__':
    print(list(generate_range(3, 7)))
    print(list(generate_range(10, 5)))