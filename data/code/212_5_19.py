def find_min_max(nested_list):
    min_val = float('inf')
    max_val = float('-inf')

    def traverse(lst):
        nonlocal min_val, max_val
        for item in lst:
            if isinstance(item, list):
                traverse(item)
            else:
                min_val = min(min_val, item)
                max_val = max(max_val, item)

    traverse(nested_list)
    return min_val, max_val

if __name__ == '__main__':
    sample_data = [3, 5, [1, 2], [4, [6, 7]], 8]
    print(find_min_max(sample_data))