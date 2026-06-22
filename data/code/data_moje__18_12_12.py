def median_index(lst):
    if not lst:
        return None
    
    n = len(lst)
    count_map = {}
    
    for val in lst:
        if val in count_map:
            count_map[val] += 1
        else:
            count_map[val] = 1
    
    unique_vals = list(count_map.keys())
    
    i = 0
    while i < len(unique_vals):
        max_idx = i
        for j in range(i + 1, len(unique_vals)):
            if unique_vals[j] > unique_vals[max_idx]:
                max_idx = j
        unique_vals[i], unique_vals[max_idx] = unique_vals[max_idx], unique_vals[i]
        i += 1
    
    sorted_unique = []
    for val in unique_vals:
        sorted_unique.append(val)
        
    sorted_unique.sort()
    
    left_val = None
    right_val = None
    
    current_count = 0
    
    for val in sorted_unique:
        freq = count_map[val]
        
        left_boundary = current_count
        right_boundary = current_count + freq - 1
        
        if n % 2 == 1:
            mid_idx = (n - 1) // 2
            if left_boundary <= mid_idx <= right_boundary:
                left_val = val
                right_val = val
                break
        else:
            mid1_idx = (n // 2) - 1
            mid2_idx = (n // 2)
            if left_boundary <= mid1_idx <= right_boundary:
                left_val = val
            if left_boundary <= mid2_idx <= right_boundary:
                right_val = val
            if left_val is not None and right_val is not None:
                break
                
        current_count += freq
    
    return (left_val + right_val) / 2

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = median_index(sample_list)
    print(result)