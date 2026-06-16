def cycle_range(start, end):
    if start <= end:
        for i in range(start, end + 1):
            yield i
    elif end < start:
        for i in range(end, start - 1, -1):
            yield i
if __name__ == '__main__':
    print("Testing cycle_range(1, 5):")
    for num in cycle_range(1, 5):
        print(num)
    print("\nTesting cycle_range(10, 8):")
    for num in cycle_range(10, 8):
        print(num)
    print("\nTesting cycle_range(5, 5):")
    for num in cycle_range(5, 5):
        print(num)