def find_min_max_nested(nested_list):
    if not nested_list:
        return None, None
    
    def traverse(lst):
        nonlocal minimum, maximum
        for item in lst:
            if isinstance(item, list):
                traverse(item)
            else:
                if item < minimum:
                    minimum = item
                if item > maximum:
                    maximum = item
    
    minimum = float('inf')
    maximum = float('-inf')
    traverse(nested_list)
    
    return minimum, maximum

if __name__ == '__main__':
    sample_list = [3, 5, [1, 9], 2, [4, 6, [7, 8]]]
    min_val, max_val = find_min_max_nested(sample_list)
    print(f"List: {sample_list}")
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")