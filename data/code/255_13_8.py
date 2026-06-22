def find_maximum(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    
    maximum = float('-inf')
    
    for item in data:
        if isinstance(item, list):
            current_max = find_maximum(item)
        else:
            current_max = item
        
        if current_max > maximum:
            maximum = current_max
    
    return maximum

if __name__ == '__main__':
    nested_list1 = [3.14, 1.618, [2.718, 0.577, 4.669]]
    nested_list2 = [-10.5, -5.2, [-20.1, -1.9], 0]
    empty_list = []
    
    try:
        max1 = find_maximum(nested_list1)
        print(f"Maximum of {nested_list1}: {max1}")
        max2 = find_maximum(nested_list2)
        print(f"Maximum of {nested_list2}: {max2}")
        find_maximum(empty_list)
    except ValueError as e:
        print(e)