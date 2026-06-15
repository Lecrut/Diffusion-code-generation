import math
def find_min_max(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum
if __name__ == '__main__':
    sample_numbers = [15, 3, 88, 42, 9, 71]
    minimum_val, maximum_val = find_min_max(sample_numbers)
    print(f"Minimum value: {minimum_val}")
    print(f"Maximum value: {maximum_val}")