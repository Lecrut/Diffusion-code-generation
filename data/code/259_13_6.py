import math
def find_min_max(data):
    if not data:
        return None, None
    minimum = data[0]
    maximum = data[0]
    for number in data[1:]:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
    return minimum, maximum
if __name__ == '__main__':
    sample_list = [3.14159, -0.5, 100.75, -12.34, 55.0, 0.001, 99.999]
    minimum_val, maximum_val = find_min_max(sample_list)
    print(f"Sample List: {sample_list}")
    print(f"Minimum element: {minimum_val}")
    print(f"Maximum element: {maximum_val}")
    large_list = [1.0e308, -1.0e308, 5.5e290, -9.9e308]
    minimum_val_large, maximum_val_large = find_min_max(large_list)
    print(f"\nLarge List: {large_list}")
    print(f"Minimum element: {minimum_val_large}")
    print(f"Maximum element: {maximum_val_large}")
    empty_list = []
    min_empty, max_empty = find_min_max(empty_list)
    print(f"\nEmpty List: {empty_list}")
    print(f"Minimum element: {min_empty}")
    print(f"Maximum element: {max_empty}")