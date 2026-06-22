def is_iterable(item):
    return isinstance(item, (list, tuple))

def find_maximum(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    
    maximum = None
    for item in data:
        if is_iterable(item):
            current_max = find_maximum(item)
        else:
            current_max = item
        
        if maximum is None or current_max > maximum:
            maximum = current_max
    
    return maximum

if __name__ == '__main__':
    list1 = [3.14, 1.618, 2.718, 0.577]
    nested_list2 = [-10.5, -5.2, [-20.1, 1.9]]
    empty_list = []
    
    try:
        max1 = find_maximum(list1)
        print(f"Maximum of {list1}: {max1}")
        
        max2 = find_maximum(nested_list2)
        print(f"Maximum of {nested_list2}: {max2}")
        
        find_maximum(empty_list)
    except ValueError as e:
        print(e)