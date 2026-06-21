def find_min_max(nested_list):
    def recursive_search(lst):
        nonlocal minimum, maximum
        for item in lst:
            if isinstance(item, list):
                recursive_search(item)
            elif isinstance(item, (int, float)):
                if item < minimum:
                    minimum = item
                if item > maximum:
                    maximum = item

    if not nested_list:
        return None, None
    
    minimum = float('inf')
    maximum = float('-inf')
    
    recursive_search(nested_list)
    
    return minimum, maximum

if __name__ == '__main__':
    sample_list = [3, 5, [1, 2], 7, [9, [4, 8]]]
    min_val, max_val = find_min_max(sample_list)
    print(f"List: {sample_list}")
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")