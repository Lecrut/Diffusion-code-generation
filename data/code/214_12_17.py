def find_smallest_value(values):
    if not values:
        raise ValueError("Input iterable cannot be empty")
    smallest = float('inf')
    for value in values:
        if value < smallest:
            smallest = value
    return smallest

if __name__ == '__main__':
    sample1 = [3.14, 1.618, 2.718, 0.577]
    sample2 = [-10.5, 5.2, -3.14, 9.9]
    sample3 = [42.0]
    empty_set = set()

    print(f"Smallest in {sample1}: {find_smallest_value(sample1)}")
    print(f"Smallest in {sample2}: {find_smallest_value(sample2)}")
    print(f"Smallest in {sample3}: {find_smallest_value(sample3)}")
    try:
        find_smallest_value(empty_set)
    except ValueError as e:
        print(e)