def find_min_max(data):
    if not data:
        return None, None
    minimum = data[0]
    maximum = data[0]
    for element in data:
        if element < minimum:
            minimum = element
        if element > maximum:
            maximum = element
    return minimum, maximum
if __name__ == '__main__':
    large_list = [3.14159, -0.5, 100.75, -99.999, 50.0, 12345.6789]
    min_val, max_val = find_min_max(large_list)
    print(f"The list is: {large_list}")
    print(f"Minimum element: {min_val}")
    print(f"Maximum element: {max_val}")
    empty_list = []
    min_empty, max_empty = find_min_max(empty_list)
    print(f"\nTesting with an empty list:")
    print(f"Minimum element: {min_empty}")
    print(f"Maximum element: {max_empty}")