def are_lists_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    
    for item1, item2 in zip(list1, list2):
        if isinstance(item1, list) and isinstance(item2, list):
            if not are_lists_equal(item1, item2):
                return False
        elif item1 != item2:
            return False
    
    return True

if __name__ == '__main__':
    list_a = [1, 2, [3, 4], 5]
    list_b = [1, 2, [3, 4], 5]
    list_c = [1, 2, [3, 5], 5]
    list_d = [1, 2, [3, 4]]
    
    print(f"Comparing {list_a} and {list_b}: {are_lists_equal(list_a, list_b)}")
    print(f"Comparing {list_a} and {list_c}: {are_lists_equal(list_a, list_c)}")
    print(f"Comparing {list_d} and {list_a}: {are_lists_equal(list_d, list_a)}")