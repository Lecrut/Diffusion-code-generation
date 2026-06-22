def compare_adjacent_pairs(lst):
    if len(lst) < 2:
        return []
    
    result = []
    for i in range(len(lst) - 1):
        larger_value = max(lst[i], lst[i + 1])
        result.append(larger_value)
    
    return result

if __name__ == '__main__':
    sample_list_1 = [3, 6, 2, 8, 4, 7]
    sample_list_2 = [10, 5, 8, 3, 7, 9]
    sample_list_3 = [1, 2, 3, 4, 5]
    sample_list_4 = [5, 4, 3, 2, 1]
    
    print("Sample List 1:", compare_adjacent_pairs(sample_list_1))
    print("Sample List 2:", compare_adjacent_pairs(sample_list_2))
    print("Sample List 3:", compare_adjacent_pairs(sample_list_3))
    print("Sample List 4:", compare_adjacent_pairs(sample_list_4))