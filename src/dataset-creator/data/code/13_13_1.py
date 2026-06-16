def find_max(values):
    if not values:
        raise ValueError("Input list must contain at least one element.")
    max_value = values[0]
    for item in values[1:]:
        if item > max_value:
            max_value = item
    return max_value
if __name__ == '__main__':
    sample_data = [3, 7, 2, 9, 4, 85, 1]
    result = find_max(sample_data)
    print(result)