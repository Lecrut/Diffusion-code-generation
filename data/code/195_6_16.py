def compare_lists(list1, list2, key):
    comparison_results = []
    for item1, item2 in zip(list1, list2):
        try:
            if item1.get(key) == item2.get(key):
                comparison_results.append(True)
            else:
                comparison_results.append(False)
        except TypeError:
            comparison_results.append("Type Error")
    return comparison_results

if __name__ == '__main__':
    list_a = [{'id': 1, 'value': 'a'}, {'id': 2, 'value': 'b'}]
    list_b = [{'id': 1, 'value': 'a'}, {'id': 2, 'value': 'c'}]
    comparison_result = compare_lists(list_a, list_b, 'value')
    print(comparison_result)