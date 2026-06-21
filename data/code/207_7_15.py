def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

def find_max_value(nested_list):
    flat_list = flatten_list(nested_list)
    if not flat_list:
        return None
    return max(flat_list)

if __name__ == '__main__':
    nested_list1 = [3, 5, [2, 8], [1, [7, 4]]]
    result1 = find_max_value(nested_list1)
    print(f"Nested List: {nested_list1}, Max Value: {result1}")
    
    nested_list2 = [[10, 20], [30, 40], 50]
    result2 = find_max_value(nested_list2)
    print(f"Nested List: {nested_list2}, Max Value: {result2}")
    
    nested_list3 = []
    result3 = find_max_value(nested_list3)
    print(f"Nested List: {nested_list3}, Max Value: {result3}")