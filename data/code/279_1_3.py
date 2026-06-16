def cycle_range(start, end):
    if start > end:
        return
    current = start
    while current <= end:
        yield current
        current += 1
if __name__ == '__main__':
    print("Testing cycle_range(1, 5):")
    for number in cycle_range(1, 5):
        print(number)
    print("\nTesting cycle_range(10, 8):")
    for number in cycle_range(10, 8):
        print(number)
    print("\nTesting cycle_range(5, 5):")
    for number in cycle_range(5, 5):
        print(number)