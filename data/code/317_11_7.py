def cycle_range(start, end):
    if start > end:
        return
    for i in range(start, end + 1):
        yield i
if __name__ == '__main__':
    print("Testing cycle_range(1, 5):")
    for num in cycle_range(1, 5):
        print(num)
    print("\nTesting cycle_range(10, 8):")
    for num in cycle_range(10, 8):
        print(num)
    print("\nTesting cycle_range(0, 3):")
    for num in cycle_range(0, 3):
        print(num)