def cycle_range(start, end):
    current = start
    while current <= end:
        yield current
        current += 1
if __name__ == '__main__':
    print(list(cycle_range(5, 10)))
    print(list(cycle_range(0, -3)))
    print(list(cycle_range(10, 10)))