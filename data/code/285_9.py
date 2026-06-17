import operator
def compare_adjacent_elements(data, key):
    results = []
    for i in range(len(data) - 1):
        val1 = data[i][key]
        val2 = data[i+1][key]
        comparison_result = operator.lt(val1, val2) if key in ['<', '>', '='] else (val1 < val2) if key == '<' else (val1 > val2) if key == '>' else (val1 == val2)
        results.append((data[i], data[i+1], comparison_result))
    return results
if __name__ == '__main__':
    sample_list = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 25},
        {'id': 3, 'value': 15},
        {'id': 4, 'value': 30}
    ]
    print("Comparing based on 'value' using '<' operator:")
    comparison_results_lt = compare_adjacent_elements(sample_list, 'value')
    for item in comparison_results_lt:
        print(f"Item 1: {item[0]} vs Item 2: {item[1]}, Result: {item[2]}")
    print("\nComparing based on '>' operator:")
    comparison_results_gt = compare_adjacent_elements(sample_list, 'value')
    for item in comparison_results_gt:
        print(f"Item 1: {item[0]} vs Item 2: {item[1]}, Result: {item[2]}")
    print("\nComparing based on '=' operator:")
    comparison_results_eq = compare_adjacent_elements(sample_list, 'value')
    for item in comparison_results_eq:
        print(f"Item 1: {item[0]} vs Item 2: {item[1]}, Result: {item[2]}")