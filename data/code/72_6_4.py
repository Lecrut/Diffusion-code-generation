def compare_lists(list1, list2):
    results = []
    for item1, item2 in zip(list1, list2):
        if item1 > item2:
            results.append(f"{item1} > {item2}")
        elif item1 < item2:
            results.append(f"{item1} < {item2}")
        else:
            results.append(f"{item1} == {item2}")
    return results

if __name__ == '__main__':
    list_a = [1, 5, 10, 15]
    list_b = [2, 4, 10, 20]
    comparison_results = compare_lists(list_a, list_b)
    for result in comparison_results:
        print(result)