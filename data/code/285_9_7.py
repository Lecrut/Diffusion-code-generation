import operator
def compare_adjacent_elements(data, key):
    results = []
    for i in range(len(data) - 1):
        item1 = data[i]
        item2 = data[i+1]
        try:
            comparison_result = operator.gt(item1[key], item2[key]) if key in item1 and key in item2 else (operator.lt(item1[key], item2[key]) if key in item1 and key in item2 else None)
            results.append(comparison_result)
        except TypeError:
            results.append("Comparison Error")
    return results
if __name__ == '__main__':
    list_a = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 5},
        {'id': 3, 'value': 20},
        {'id': 4, 'value': 15}
    ]
    key_to_compare = 'value'
    comparison_results = compare_adjacent_elements(list_a, key_to_compare)
    print(comparison_results)