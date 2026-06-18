def max_weight_difference(*collections):
    all_elements = []
    for collection in collections:
        if isinstance(collection, (list, tuple)):
            all_elements.extend(collection)
    if not all_elements:
        return 0
    min_val = float('inf')
    max_val = float('-inf')
    for elem in all_elements:
        try:
            num_elem = int(elem)
        except (ValueError, TypeError):
            continue
        if num_elem < min_val:
            min_val = num_elem
        elif num_elem > max_val:
            max_val = num_elem
    return abs(max_val - min_val)
if __name__ == '__main__':
    sample_data_1 = [5, 20, 3]
    sample_data_2 = [-10, 45, 8]
    result = max_weight_difference(sample_data_1, sample_data_2)
    print(result)