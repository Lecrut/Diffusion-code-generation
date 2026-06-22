def compare_adjacent_pairs(lst):
    if len(lst) < 2:
        return []
    
    result = []
    for i in range(len(lst) - 1):
        result.append(max(lst[i], lst[i + 1]))
    
    return result

if __name__ == '__main__':
    sample_list = [3, 6, 2, 8, 4, 7]
    print(compare_adjacent_pairs(sample_list))