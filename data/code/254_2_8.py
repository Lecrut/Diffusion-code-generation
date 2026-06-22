def find_minimum(nested_list):
    min_val = float('inf')
    for item in nested_list:
        if isinstance(item, list):
            current_min = find_minimum(item)
            if current_min < min_val:
                min_val = current_min
        elif isinstance(item, (int, float)) and item < min_val:
            min_val = item
    return min_val

if __name__ == '__main__':
    sample_data = [3, 5, [1, 2], [4, [6, 7]], 0]
    print(find_minimum(sample_data))