def find_min_max(nested_list):
    if not isinstance(nested_list, list) or not nested_list:
        raise ValueError("Input must be a non-empty list.")
    
    min_val = float('inf')
    max_val = float('-inf')
    
    def traverse(sublist):
        nonlocal min_val, max_val
        for item in sublist:
            if isinstance(item, list):
                traverse(item)
            else:
                if item < min_val:
                    min_val = item
                if item > max_val:
                    max_val = item
    
    traverse(nested_list)
    return min_val, max_val

if __name__ == '__main__':
    sample_data = [10, [5, 20], [3, [15, 25]]]
    print(find_min_max(sample_data))