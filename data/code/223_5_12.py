def find_max_coerced(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    max_value = None
    for item in data:
        if max_value is None or (isinstance(item, int) and isinstance(max_value, int)) and item > max_value:
            max_value = item
        elif isinstance(item, float) and isinstance(max_value, float) and item > max_value:
            max_value = item
    
    return max_value

if __name__ == '__main__':
    list1 = [3.14, 2.718, 1.618, 4]
    list2 = [-5.5, -1.2, -8.9, -3]
    list3 = [100.0, 50, 150, 75]
    list4 = [0, -1, 0]
    empty_list = []
    
    print(f"Max of {list1}: {find_max_coerced(list1)}")
    print(f"Max of {list2}: {find_max_coerced(list2)}")
    print(f"Max of {list3}: {find_max_coerced(list3)}")
    print(f"Max of {list4}: {find_max_coerced(list4)}")