def are_lists_equal(list_a, list_b):
    return set(list_a) == set(list_b)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [1, 2, 5, 4]
    list3 = [1, 2, 3, 4]
    list4 = [1, 2, 3]

    result1 = are_lists_equal(list1, list2)
    print(f"Comparing {list1} and {list2}: Equality={result1}")

    result2 = are_lists_equal(list1, list3)
    print(f"Comparing {list1} and {list3}: Equality={result2}")