def max_weight_difference(*collections):
    all_elements = []
    for collection in collections:
        if isinstance(collection, (list, tuple)):
            all_elements.extend(collection)
    if not all_elements:
        return 0
    min_val = float('inf')
    max_val = float('-inf')
    for val in all_elements:
        if val < min_val:
            min_val = val
        elif val > max_val:
            max_val = val
    return max_val - min_val
if __name__ == '__main__':
    sample_data_1 = [5, 20, 3]
    sample_data_2 = (42, 9)
    result = max_weight_difference(sample_data_1, sample_data_2)
    print(result)