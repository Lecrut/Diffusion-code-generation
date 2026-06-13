def compare_lists(list1, list2):
    results = []
    for item1, item2 in zip(list1, list2):
        try:
            if item1 == item2:
                results.append(True)
            else:
                results.append(False)
        except TypeError:
            results.append("Type Error")
    return results
if __name__ == '__main__':
    list_a = [1, 2, 'a', 4.0]
    list_b = [1, 2, 'a', 5.0]
    list_c = [1, 2, 3, 4]
    print("Comparing list_a and list_b:")
    comparison_ab = compare_lists(list_a, list_b)
    print(comparison_ab)
    print("\nComparing list_a and list_c (testing TypeError):")
    comparison_ac = compare_lists(list_a, list_c)
    print(comparison_ac)
    list_d = [1, 2, 'hello']
    list_e = [1, 2, 3]
    print("\nComparing list_d and list_e (testing mixed types):")
    comparison_de = compare_lists(list_d, list_e)
    print(comparison_de)