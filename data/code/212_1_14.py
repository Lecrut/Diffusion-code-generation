def find_min_max(data):
    if not data:
        return None, None
    minimum = maximum = data[0]
    for num in data[1:]:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num
    return minimum, maximum

if __name__ == '__main__':
    large_list = [3.1415926535, -0.5, 100.75, -99.999, 50.0]
    min_val, max_val = find_min_max(large_list)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")

    another_list = [1.0, 2.5, -3.2, 4.8, 0.9]
    min_val_2, max_val_2 = find_min_max(another_list)
    print(f"Minimum: {min_val_2}")
    print(f"Maximum: {max_val_2}")

    empty_list = []
    min_val_3, max_val_3 = find_min_max(empty_list)
    print(f"Empty list result (Min): {min_val_3}")