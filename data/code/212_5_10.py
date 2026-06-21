def find_min_max(nested_list):
    if isinstance(nested_list, list):
        min_val = float('inf')
        max_val = float('-inf')
        for item in nested_list:
            sub_min, sub_max = find_min_max(item)
            min_val = min(min_val, sub_min)
            max_val = max(max_val, sub_max)
        return min_val, max_val
    else:
        return nested_list, nested_list

if __name__ == '__main__':
    sample_data = [3, [1, 2], [5, [4, 6]], 7]
    min_val, max_val = find_min_max(sample_data)
    print(f"Minimum: {min_val}, Maximum: {max_val}")