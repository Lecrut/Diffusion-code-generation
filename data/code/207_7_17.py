def find_max_in_nested_list(nested_list):
    if not all(isinstance(item, (list, int)) for item in nested_list):
        raise ValueError("Input must be a nested list containing integers or other lists")
    flat_list = [item for sublist in nested_list for item in (find_max_in_nested_list(sublist) if isinstance(item, list) else [item])]
    return max(flat_list)

if __name__ == '__main__':
    sample1 = [[3, 5], [2, [8]], 9]
    result1 = find_max_in_nested_list(sample1)
    print(f"Nested List: {sample1}, Max: {result1}")
    
    sample2 = [[-1, -3], [-2, [-4]], 0]
    result2 = find_max_in_nested_list(sample2)
    print(f"Nested List: {sample2}, Max: {result2}")
    
    sample3 = [[5], [5], 5]
    result3 = find_max_in_nested_list(sample3)
    print(f"Nested List: {sample3}, Max: {result3}")