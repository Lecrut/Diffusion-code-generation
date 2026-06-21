def flatten_and_find_largest(nested_list):
    flattened = []
    for sublist in nested_list:
        for item in sublist:
            flattened.append(item)
    if not flattened:
        raise ValueError("Flattened list cannot be empty")
    largest = flattened[0]
    for number in flattened[1:]:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    nested_list1 = [[34, 2], [78, 9], [56]]
    nested_list2 = [[-1, -2], [-3, -4], [-5, -6]]
    nested_list3 = []
    
    print(f"Largest in {nested_list1}: {flatten_and_find_largest(nested_list1)}")
    print(f"Largest in {nested_list2}: {flatten_and_find_largest(nested_list2)}")
    try:
        print(f"Largest in {nested_list3}: {flatten_and_find_largest(nested_list3)}")
    except ValueError as e:
        print(e)