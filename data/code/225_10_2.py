import math
def find_min_max(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum
if __name__ == '__main__':
    data = [15, 8, 22, 4, 30, 11]
    minimum_val, maximum_val = find_min_max(data)
    print(f"Minimum value: {minimum_val}")
    print(f"Maximum value: {maximum_val}")