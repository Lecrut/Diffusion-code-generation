def max_weight_difference(*collections):
    all_elements = []
    for collection in collections:
        if isinstance(collection, (list, tuple)):
            all_elements.extend(collection)
        elif hasattr(collection, '__iter__') and not isinstance(collection, str):
            try:
                all_elements.extend(list(collection))
            except TypeError:
                pass
    if len(all_elements) < 2:
        return None
    max_val = max(all_elements)
    min_val = min(all_elements)
    return abs(max_val - min_val)
if __name__ == '__main__':
    sample_data_1 = [5, 3, 9]
    sample_data_2 = (7.5, 4.2, 8.0)
    result = max_weight_difference(sample_data_1, sample_data_2)
    print(result)