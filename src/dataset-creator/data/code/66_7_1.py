def max_weight_difference(*collections):
    all_elements = []
    for collection in collections:
        if isinstance(collection, (list, tuple)):
            all_elements.extend(collection)
    if not all_elements:
        return 0
    min_val = float('inf')
    max_val = float('-inf')
    for element in all_elements:
        try:
            val = float(element)
            if val < min_val:
                min_val = val
            elif val > max_val:
                max_val = val
        except (ValueError, TypeError):
            continue
    return abs(max_val - min_val)
if __name__ == '__main__':
    sample_data = [10, 25], [-5, 30.5], [7]
    result = max_weight_difference(*sample_data)
    print(result)