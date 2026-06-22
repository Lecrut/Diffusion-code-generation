def compare_adjacent_pairs(lst):
    if len(lst) < 2:
        return []
    
    result = []
    for i in range(len(lst) - 1):
        result.append(max(lst[i], lst[i + 1]))
    
    return result

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(compare_adjacent_pairs(sample_list))