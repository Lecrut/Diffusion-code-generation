def evaluate_expression(input_list):
    results = []
    for record in input_list:
        var_map = dict(record)
        val_a = var_map.get('A', False)
        val_b = var_map.get('B', False)
        val_c = var_map.get('C', False)
        val_d = var_map.get('D', False)
        left_term = val_a and val_b
        if left_term:
            results.append(True)
            continue
        right_term = val_c and not val_d
        results.append(right_term)
    return results

if __name__ == '__main__':
    test_data = [
        [('A', True), ('B', True), ('C', True), ('D', True)],
        [('A', False), ('B', True), ('C', False), ('D', False)],
        [('A', True), ('B', False), ('C', True), ('D', False)],
        [('A', False), ('B', False), ('C', True), ('D', True)],
    ]
    print(evaluate_expression(test_data))