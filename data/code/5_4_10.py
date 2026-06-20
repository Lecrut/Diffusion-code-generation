def compare_length_lists(list1, list2):
    all_values = list1 + list2
    min_val = min(all_values)
    max_val = max(all_values)
    range_diff = max_val - min_val
    return {
        'min': min_val,
        'max': max_val,
        'range': range_diff
    }

if __name__ == '__main__':
    lengths1 = [1.5, 2.3, 3.1]
    lengths2 = [0.9, 4.2, 2.3]
    result = compare_length_lists(lengths1, lengths2)
    print(result)