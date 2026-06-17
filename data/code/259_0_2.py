import math
def find_min_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    smallest = data[0]
    largest = data[0]
    for x in data:
        if x < smallest:
            smallest = x
        if x > largest:
            largest = x
    return smallest, largest
if __name__ == '__main__':
    sample_list = [34, 12, 56, 89, 23, 77]
    min_val, max_val = find_min_max(sample_list)
    print(f"Smallest value: {min_val}")
    print(f"Largest value: {max_val}")