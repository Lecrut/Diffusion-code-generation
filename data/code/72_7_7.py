def elements_ordered_at(list_a, list_b, pos):
    len_a = len(list_a)
    len_b = len(list_b)
    if pos < 0:
        raise ValueError("Index must be non-negative")
    if pos >= len_a:
        raise ValueError("Index out of range for first list")
    if pos >= len_b:
        raise ValueError("Index out of range for second list")
    return list_a[pos] <= list_b[pos]

if __name__ == '__main__':
    sample_first = [5, 15, 25]
    sample_second = [10, 12, 30]
    sample_index = 0
    comparison_result = elements_ordered_at(sample_first, sample_second, sample_index)
    print(comparison_result)