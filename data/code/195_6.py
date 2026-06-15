def compare_lists(list1, list2):
    comparison_results = []
    for item1, item2 in zip(list1, list2):
        try:
            if item1 == item2:
                comparison_results.append(True)
            else:
                comparison_results.append(False)
        except TypeError:
            comparison_results.append("Type Error")
    return comparison_results
if __name__ == '__main__':
    list_a = [1, "a", 3.0, None]
    list_b = [1, "a", 3.0, 4]
    list_c = [1, "a", 3.0, "b"]
    print("Comparing list_a and list_b:")
    result1 = compare_lists(list_a, list_b)
    print(result1)
    print("\nComparing list_a and list_c:")
    result2 = compare_lists(list_a, list_c)
    print(result2)
    list_d = [1, 2]
    list_e = [3, "x"]
    print("\nComparing list_d and list_e:")
    result3 = compare_lists(list_d, list_e)
    print(result3)