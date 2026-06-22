def find_min_max(nested_list):
    current_min = float('inf')
    current_max = float('-inf')
    
    def traverse(sublist):
        nonlocal current_min, current_max
        for item in sublist:
            if isinstance(item, list):
                traverse(item)
            else:
                if item < current_min:
                    current_min = item
                if item > current_max:
                    current_max = item
    
    traverse(nested_list)
    return current_min, current_max

if __name__ == '__main__':
    sample_data = [10, 5, [20, 3], [15, [25]]]
    min_val, max_val = find_min_max(sample_data)
    print(f"Min: {min_val}, Max: {max_val}")