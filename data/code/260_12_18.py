def compare_lists(list1, list2):
    if not all(isinstance(item, float) for item in list1 + list2):
        raise ValueError("Both lists must contain only floating-point numbers.")
    
    intersection = set(list1).intersection(set(list2))
    unique_in_list1 = set(list1) - intersection
    unique_in_list2 = set(list2) - intersection
    
    return sorted(unique_in_list1), sorted(unique_in_list2)

if __name__ == '__main__':
    list_a = [1.0, 2.5, 3.3, 4.7, 5.1]
    list_b = [3.3, 4.7, 5.1, 6.9, 7.2]
    
    result = compare_lists(list_a, list_b)
    print(f"Difference in List A: {result[0]}")
    print(f"Difference in List B: {result[1]}")