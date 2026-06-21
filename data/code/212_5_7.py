def find_min_max_values(nested_list):
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

    min_val = float('inf')
    max_val = float('-inf')
    traverse(nested_list)
    return min_val, max_val

if __name__ == '__main__':
    sample_list = [3, [1, 4], [2, [5, 6]], 7]
    min_val, max_val = find_min_max_values(sample_list)
    print(f"List: {sample_list}")
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")