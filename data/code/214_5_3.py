import math
def find_absolute_minimum(iterable):
    if not iterable:
        raise ValueError("Iterable cannot be empty")
    iterator = iter(iterable)
    try:
        min_val = next(iterator)
    except StopIteration:
        raise ValueError("Iterable is empty")
    for value in iterator:
        if value < min_val:
            min_val = value
    return min_val
if __name__ == '__main__':
    sample1 = [3, 1, 4, 1, 5, 9, 2]
    print(f"Sample 1: {find_absolute_minimum(sample1)}")
    sample2 = (7.5, 1.2, 8.0, -3.5, 0.1)
    print(f"Sample 2: {find_absolute_minimum(sample2)}")
    sample3 = [100]
    print(f"Sample 3: {find_absolute_minimum(sample3)}")
    sample4 = [-5, -10, -1, -20]
    print(f"Sample 4: {find_absolute_minimum(sample4)}")
    sample5 = []
    try:
        find_absolute_minimum(sample5)
    except ValueError as e:
        print(f"Sample 5 Error: {e}")