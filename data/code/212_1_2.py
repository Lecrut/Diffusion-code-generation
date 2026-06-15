def find_min_max(data):
    if not data:
        return None, None
    minimum = min(data)
    maximum = max(data)
    return minimum, maximum
if __name__ == '__main__':
    large_list = [3.1415926535, -0.5, 100.75, -99.999, 50.0]
    minimum_val, maximum_val = find_min_max(large_list)
    print(f"Minimum: {minimum_val}")
    print(f"Maximum: {maximum_val}")
    another_list = [1.23e-10, 4567890123.45, -1.0]
    minimum_val_2, maximum_val_2 = find_min_max(another_list)
    print(f"Minimum: {minimum_val_2}")
    print(f"Maximum: {maximum_val_2}")
    empty_list = []
    minimum_val_3, maximum_val_3 = find_min_max(empty_list)
    print(f"Empty List Minimum: {minimum_val_3}")
    print(f"Empty List Maximum: {maximum_val_3}")