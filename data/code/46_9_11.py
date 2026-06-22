def flatten_and_find_max(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_and_find_max(item))
        else:
            flattened.append(item)
    if not flattened:
        return None
    return max(flattened)

if __name__ == '__main__':
    sample_data = [
        [1000, 2000, [3000, 4000]],
        [5000, [6000, 7000, [8000, 9000]]],
        [100, 200]
    ]
    result = flatten_and_find_max(sample_data)
    print(result)