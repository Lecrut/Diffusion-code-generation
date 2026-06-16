import operator
def compare_adjacent_elements(data, key):
    result = []
    for i in range(len(data) - 1):
        item1 = data[i]
        item2 = data[i+1]
        try:
            comparison_result = operator.gt(item1[key], item2[key]) if key in item1 and key in item2 else (operator.lt(item1[key], item2[key]) if key in item1 and key in item2 else None)
            if comparison_result is not None:
                result.append(comparison_result)
        except TypeError:
            continue
    return result
if __name__ == '__main__':
    list_a = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 5},
        {'id': 3, 'value': 15},
        {'id': 4, 'value': 8}
    ]
    list_b = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 6},
        {'id': 3, 'value': 15},
        {'id': 4, 'value': 8}
    ]
    list_c = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 4},
        {'id': 3, 'value': 15},
        {'id': 4, 'value': 8}
    ]
    key_to_compare = 'value'
    result_ab = compare_adjacent_elements(list_a, key_to_compare)
    print(f"Comparison between list_a and list_b (key='{key_to_compare}'): {result_ab}")
    result_ac = compare_adjacent_elements(list_a, key_to_compare)
    print(f"Comparison between list_a and list_c (key='{key_to_compare}'): {result_ac}")