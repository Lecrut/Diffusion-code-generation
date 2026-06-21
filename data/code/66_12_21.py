def compare_adjacent_pairs(lst):
    if len(lst) < 2:
        return []
    
    result = []
    for i in range(len(lst) - 1):
        first, second = lst[i], lst[i + 1]
        larger_value = max(first, second)
        result.append(larger_value)
    
    return result

if __name__ == '__main__':
    sample_list = [5, 9, 3, 7, 6, 2]
    comparison_result = compare_adjacent_pairs(sample_list)
    print(comparison_result)