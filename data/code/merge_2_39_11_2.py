def find_max_value(iterable):
    if not hasattr(iterable, '__iter__'):
        raise TypeError("Input must be an iterable")
    max_value = None
    for item in iterable:
        if max_value is None or item > max_value:
            max_value = item
    if max_value is None:
        raise ValueError("max() arg is an empty sequence")
    return max_value
if __name__ == '__main__':
    sample_data_1 = [3, 7, 2, 9, 4]
    sample_data_2 = "python"
    sample_data_3 = []
    print(f"Max of {sample_data_1}:")
    result_1 = find_max_value(sample_data_1)
    print(result_1)
    print(f"\nMax of '{sample_data_2}':")
    result_2 = find_max_value(sample_data_2)
    print(repr(result_2))
    try:
        result_3 = find_max_value(sample_data_3)
    except ValueError as e:
        print(f"Error for empty list: {e}")