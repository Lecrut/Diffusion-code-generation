def compare_number_sets(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    if set1 == set2:
        intersection = len(set1)
        return (True, intersection)
    else:
        intersection = len(set1.intersection(set2))
        return (False, intersection)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [5, 4, 3, 2, 1]
    list_c = [1, 2, 3, 5]
    list_d = [1, 2, 3, 4, 5, 6]
    result1 = compare_number_sets(list_a, list_b)
    print(f"Comparing {list_a} and {list_b}: {result1}")
    result2 = compare_number_sets(list_a, list_c)
    print(f"Comparing {list_a} and {list_c}: {result2}")
    result3 = compare_number_sets(list_a, list_d)
    print(f"Comparing {list_a} and {list_d}: {result3}")