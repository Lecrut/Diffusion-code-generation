def find_min_max(data):
    if not data:
        return None, None
    minimum = min(data)
    maximum = max(data)
    return minimum, maximum
if __name__ == '__main__':
    large_list = [3.14159, -0.5, 100.75, -12.34, 55.0, 0.001, 99.999]
    minimum_val, maximum_val = find_min_max(large_list)
    print(f"Minimum: {minimum_val}")
    print(f"Maximum: {maximum_val}")
    empty_list = []
    min_val_empty, max_val_empty = find_min_max(empty_list)
    print(f"Empty List Minimum: {min_val_empty}")
    print(f"Empty List Maximum: {max_val_empty}")