def generate_range(start, end):
    if start > end:
        start, end = end, start
    while start <= end:
        yield start
        start += 1

if __name__ == '__main__':
    for number in generate_range(5, 10):
        print(number)