def compare_lists(list1, list2):
    comparison_map = {
        True: f"{item1} == {item2}",
        False: lambda item1, item2: f"{item1} != {item2}"
    }
    return [comparison_map[item1 == item2](item1, item2) for item1, item2 in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [5, 9, 14, 19]
    sample_list2 = [3, 9, 16, 18]
    results = compare_lists(sample_list1, sample_list2)
    for result in results:
        print(result)