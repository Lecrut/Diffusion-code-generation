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
            results.append(comparison_result)
        except TypeError:
            results.append("Comparison Error")
    return results
if __name__ == '__main__':
    list_a = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 25},
        {'id': 3, 'value': 5}
    ]
    list_b = [
        {'id': 4, 'value': 15},
        {'id': 5, 'value': 30},
        {'id': 6, 'value': 8}
    ]
    print("Comparing list_a and list_b based on 'value':")
    comparison_results = compare_adjacent_elements(list_a, 'value')
    print(comparison_results)
    print("\nComparing list_a based on 'id':")
    comparison_results_id = compare_adjacent_elements(list_a, 'id')
    print(comparison_results_id)
    list_c = [
        {'x': 100},
        {'x': 50}
    ]
    print("\nComparing list_c based on 'x':")
    comparison_results_c = compare_adjacent_elements(list_c, 'x')
    print(comparison_results_c)