def find_min_max(data):
    if not data:
        return None, None
    minimum = min(data)
    maximum = max(data)
    return minimum, maximum
if __name__ == '__main__':
    large_list = [3.1415926535, -10.5, 0.001, 99.99999999, -123.456789]
    minimum_val, maximum_val = find_min_max(large_list)
    print(f"Minimum: {minimum_val}")
    print(f"Maximum: {maximum_val}")
    empty_list = []
    min_empty, max_empty = find_min_max(empty_list)
    print(f"Empty List Minimum: {min_empty}")
    print(f"Empty List Maximum: {max_empty}")