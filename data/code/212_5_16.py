def find_min_max_values(nested_list):
    if not nested_list:
        return None, None
    
    def traverse(lst):
        if isinstance(lst, list):
            for item in lst:
                yield from traverse(item)
        else:
            yield lst
    
    values = list(traverse(nested_list))
    
    minimum = min(values)
    maximum = max(values)
    
    return minimum, maximum

if __name__ == '__main__':
    sample_list = [[3, 5], [1, 2, [4]], 6]
    min_val, max_val = find_min_max_values(sample_list)
    print(f"List: {sample_list}")
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")

    sample_list_2 = [[10, 20], [30, [40, 50]], 60]
    min_val, max_val = find_min_max_values(sample_list_2)
    print(f"List: {sample_list_2}")
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")