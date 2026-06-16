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
    list1 = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 25},
        {'id': 3, 'value': 15},
        {'id': 4, 'value': 30}
    ]
    list2 = [
        {'a': 100, 'b': 5},
        {'a': 105, 'b': 6},
        {'a': 98, 'b': 7},
        {'a': 110, 'b': 8}
    ]
    list3 = [
        {'x': 1, 'y': 5},
        {'x': 2, 'y': 6},
        {'x': 3, 'y': 7}
    ]
    print("--- Comparing list1 by 'value' ---")
    result1 = compare_adjacent_elements(list1, 'value')
    print(result1)
    print("\n--- Comparing list2 by 'a' ---")
    result2 = compare_adjacent_elements(list2, 'a')
    print(result2)
    print("\n--- Comparing list3 by 'y' ---")
    result3 = compare_adjacent_elements(list3, 'y')
    print(result3)