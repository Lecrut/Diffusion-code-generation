def find_extremes(nested_list):
    if isinstance(nested_list[0], list):
        return find_extremes(nested_list[0]), find_extremes(nested_list[1:])
    else:
        return nested_list, nested_list

def process_nested_list(nested_list):
    min_val, max_val = find_extremes(nested_list)
    min_val = min(min_val) if isinstance(min_val, tuple) else min_val
    max_val = max(max_val) if isinstance(max_val, tuple) else max_val
    return min_val, max_val

if __name__ == '__main__':
    sample_data = [[1, 2, [3]], 4, [5, [6, 7], 8]]
    result = process_nested_list(sample_data)
    print(result)