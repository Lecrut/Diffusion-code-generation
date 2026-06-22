def compare_min_max(list1, list2):
    if not all(isinstance(x, (int, float)) for x in list1 + list2):
        raise ValueError("Both lists must contain only numbers")
    
    min_list1 = min(list1) if list1 else None
    max_list1 = max(list1) if list1 else None
    min_list2 = min(list2) if list2 else None
    max_list2 = max(list2) if list2 else None
    
    return {
        "min_list1": min_list1,
        "max_list1": max_list1,
        "min_list2": min_list2,
        "max_list2": max_list2
    }

if __name__ == '__main__':
    result = compare_min_max([3, 5, 1], [4, 7, 2])
    print(result)