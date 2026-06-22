def is_valid_data(data):
    if not isinstance(data, list) or not all(isinstance(item, (int, list)) for item in data):
        return False
    return True

def find_min_max(data, minimum=float('inf'), maximum=-float('inf')):
    if not is_valid_data(data):
        raise ValueError("Invalid data structure")

    for item in data:
        if isinstance(item, list):
            min_val, max_val = find_min_max(item, minimum, maximum)
            if min_val < minimum:
                minimum = min_val
            if max_val > maximum:
                maximum = max_val
        else:
            if item < minimum:
                minimum = item
            if item > maximum:
                maximum = item

    return minimum, maximum

if __name__ == '__main__':
    sample_data = [3, [1, 4], [5, 9, [2, 6]]]
    min_val, max_val = find_min_max(sample_data)
    print(f"Minimum: {min_val}, Maximum: {max_val}")