import math
def find_absolute_minimum(iterable):
    try:
        iterator = iter(iterable)
        first_value = next(iterator)
    except StopIteration:
        raise ValueError("Iterable is empty")
    minimum = first_value
    for value in iterator:
        if value < minimum:
            minimum = value
    return minimum
if __name__ == '__main__':
    sample1 = [3, 1, 4, 1, 5, 9, 2]
    print(f"Sample 1: {find_absolute_minimum(sample1)}")
    sample2 = (x for x in [10, -5, 20, -100, 3])
    print(f"Sample 2: {find_absolute_minimum(sample2)}")
    sample3 = [42]
    print(f"Sample 3: {find_absolute_minimum(sample3)}")
    sample4 = []
    try:
        print(f"Sample 4: {find_absolute_minimum(sample4)}")
    except ValueError as e:
        print(f"Sample 4 Error: {e}")