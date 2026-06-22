def find_min_max(nested_list):
    if isinstance(nested_list, list):
        return min(find_min_max(item) for item in nested_list), max(find_min_max(item) for item in nested_list)
    else:
        return nested_list, nested_list

if __name__ == '__main__':
    sample = [3, [1, 2], [4, [5, 6]]]
    min_val, max_val = find_min_max(sample)
    print(f"Minimum: {min_val}, Maximum: {max_val}")