def range_generator(start, end):
    current = start
    while current <= end:
        yield current
        current += 1
if __name__ == '__main__':
    start_val = 5
    end_val = 15
    generator = range_generator(start_val, end_val)
    for number in generator:
        print(number)