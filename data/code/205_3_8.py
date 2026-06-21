def iter_min_sort(data):
    if not all(isinstance(x, int) for x in data):
        raise ValueError("All elements must be integers.")
    
    sorted_list = []
    while data:
        min_val = min(data)
        sorted_list.append(min_val)
        data.remove(min_val)
    
    return sorted_list

if __name__ == '__main__':
    sample_data = [3, 1, 5, 2, 8]
    sorted_result = iter_min_sort(sample_data)
    print(sorted_result)