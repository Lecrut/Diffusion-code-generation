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
            comparison_result = operator.lt(val1, val2) if val1 is not None and val2 is not None else (operator.gt(val1, val2) if val1 is not None and val2 is not None else (operator.eq(val1, val2) if val1 is not None and val2 is not None else operator.ne(val1, val2)))
            results.append((i, comparison_result))
        except TypeError:
            results.append((i, "TypeError"))
    return results
if __name__ == '__main__':
    list_a = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 25},
        {'id': 3, 'value': 15},
        {'id': 4, 'value': 5}
    ]
    list_b = [
        {'id': 10, 'value': 100},
        {'id': 20, 'value': 90},
        {'id': 30, 'value': 100},
        {'id': 40, 'value': 50}
    ]
    print("Comparing list_a based on 'value':")
    comparison_a = compare_adjacent_elements(list_a, 'value')
    for index, result in comparison_a:
        print(f"Index {index}: Elements {list_a[index]['value']} and {list_a[index+1]['value']} -> {result}")
    print("\nComparing list_b based on 'value':")
    comparison_b = compare_adjacent_elements(list_b, 'value')
    for index, result in comparison_b:
        print(f"Index {index}: Elements {list_b[index]['value']} and {list_b[index+1]['value']} -> {result}")
    list_c = [
        {'x': 1},
        {'x': 5},
        {'x': 5}
    ]
    print("\nComparing list_c based on 'x':")
    comparison_c = compare_adjacent_elements(list_c, 'x')
    for index, result in comparison_c:
        print(f"Index {index}: Elements {list_c[index]['x']} and {list_c[index+1]['x']} -> {result}")