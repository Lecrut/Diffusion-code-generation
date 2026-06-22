def find_unique_differences(list1, list2):
    if not all(isinstance(x, float) for x in list1 + list2):
        raise ValueError("Both lists must contain only floating-point numbers.")
    
    set1 = set(list1)
    set2 = set(list2)
    
    common_elements = set1.intersection(set2)
    difference_in_list1 = sorted(list(set1 - common_elements))
    difference_in_list2 = sorted(list(set2 - common_elements))
    
    return difference_in_list1, difference_in_list2

if __name__ == '__main__':
    list_a = [1.5, 2.3, 3.7, 4.0]
    list_b = [3.7, 4.0, 5.6, 6.9]
    
    try:
        result = find_unique_differences(list_a, list_b)
        print("Unique elements in List1 but not in List2:", result[0])
        print("Unique elements in List2 but not in List1:", result[1])
    except ValueError as e:
        print(e)