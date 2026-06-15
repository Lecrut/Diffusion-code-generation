import math
def find_min_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    smallest = data[0]
    largest = data[0]
    for x in data[1:]:
        if x < smallest:
            smallest = x
        elif x > largest:
            largest = x
    return smallest, largest
if __name__ == '__main__':
    sample_list = [34, 12, 56, 89, 3, 77, 21]
    try:
        min_val, max_val = find_min_max(sample_list)
        print(f"Input list: {sample_list}")
        print(f"Smallest value: {min_val}")
        print(f"Largest value: {max_val}")
    except ValueError as e:
        print(f"Error: {e}")