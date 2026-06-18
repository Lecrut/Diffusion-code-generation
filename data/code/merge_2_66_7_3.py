def max_weight_difference(*collections):
    all_elements = []
    for col in collections:
        if isinstance(col, (list, tuple)):
            all_elements.extend(col)
    if len(all_elements) < 2:
        return None
    min_val = float('inf')
    max_val = float('-inf')
    for val in all_elements:
        try:
            num = int(val)
        except (ValueError, TypeError):
            continue
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return max_val - min_val
if __name__ == '__main__':
    sample_data1 = [5, 3, 8]
    sample_data2 = [-2, 4, 7]
    result = max_weight_difference(sample_data1, sample_data2)
    print(result)