def lists_have_same_elements(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    return set_a == set_b

if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [1, 2, 5, 4]
    list3 = [1, 2, 3, 4]
    result1 = lists_have_same_elements(list1, list2)
    print(f"Comparing {list1} and {list2}: Equality={result1}")
    result2 = lists_have_same_elements(list1, list3)
    print(f"Comparing {list1} and {list3}: Equality={result2}")