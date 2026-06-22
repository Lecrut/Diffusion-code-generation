def find_min_max(list1, list2):
    min_val = float('inf')
    max_val = float('-inf')
    
    for num in list1 + list2:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    
    return min_val, max_val

if __name__ == '__main__':
    sample_list1 = [3, 5, 7, 9]
    sample_list2 = [-2, 0, 4, 6]
    
    result_min, result_max = find_min_max(sample_list1, sample_list2)
    print(f"Minimum: {result_min}, Maximum: {result_max}")