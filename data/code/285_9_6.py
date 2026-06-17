import operator
def compare_adjacent_elements(data, key):
    n = len(data)
    if n < 2:
        return []
    results = []
    for i in range(n - 1):
        val1 = data[i].get(key)
        val2 = data[i+1].get(key)
        try:
            comparison_result = operator.lt(val1, val2) if val1 is not None and val2 is not None else (operator.gt(val1, val2) if val1 is not None and val2 is not None else (operator.eq(val1, val2) if val1 is not None and val2 is not None else None))
            results.append((i, comparison_result))
        except TypeError:
            results.append((i, "Comparison Error"))
        except Exception:
            results.append((i, "Unknown Error"))
    return results
if __name__ == '__main__':
    list1 = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 25},
        {'id': 3, 'value': 15},
        {'id': 4, 'value': 30}
    ]
    key_to_compare = 'value'
    comparison_results = compare_adjacent_elements(list1, key_to_compare)
    print(comparison_results)
    list2 = [
        {'a': 1},
        {'a': 5},
        {'a': 5},
        {'a': 10}
    ]
    key_to_compare_2 = 'a'
    comparison_results_2 = compare_adjacent_elements(list2, key_to_compare_2)
    print(comparison_results_2)
    list3 = [
        {'x': 100},
        {'x': 50}
    ]
    key_to_compare_3 = 'x'
    comparison_results_3 = compare_adjacent_elements(list3, key_to_compare_3)
    print(comparison_results_3)