def find_min_max(data):
    if not data:
        return (None, None)
    minimum = float('inf')
    maximum = float('-inf')
    for item in data:
        if isinstance(item, list):
            sub_min, sub_max = find_min_max(item)
            if sub_min is not None and sub_min < minimum:
                minimum = sub_min
            if sub_max is not None and sub_max > maximum:
                maximum = sub_max
        elif isinstance(item, (int, float)):
            if item < minimum:
                minimum = item
            if item > maximum:
                maximum = item
    return (minimum, maximum)
if __name__ == '__main__':
    sample_data = [3, [1, 4, 5], 2, [8, [7, 9]]]
    result = find_min_max(sample_data)
    print(result)