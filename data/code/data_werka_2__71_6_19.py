def get_median(values):
    if not isinstance(values, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    if len(values) == 0:
        return None
    sorted_values = sorted(values)
    count = len(sorted_values)
    if count % 2 == 1:
        return sorted_values[count // 2]
    else:
        return sorted_values[(count // 2) - 1]

if __name__ == '__main__':
    sample_odd = [3, 1, 4, 1, 5, 9, 2]
    sample_even = [10, 20, 30, 40]
    sample_single = [42]
    sample_empty = []

    result_odd = get_median(sample_odd)
    result_even = get_median(sample_even)
    result_single = get_median(sample_single)
    result_empty = get_median(sample_empty)

    print(result_odd)
    print(result_even)
    print(result_single)
    print(result_empty)