def evaluate_expression(input_list):
    left_term = None
    right_term = None
    final_results = []
    for record in input_list:
        var_map = dict(record)
        val_a = var_map.get('A', False)
        val_b = var_map.get('B', False)
        val_c = var_map.get('C', False)
        val_d = var_map.get('D', False)
        left_term = val_a and val_b
        right_term = val_c and not val_d
        final_results.append(left_term or right_term)
    return final_results

if __name__ == '__main__':
    test_data = [
        [('A', True), ('B', True), ('C', True), ('D', True)],
        [('A', False), ('B', True), ('C', False), ('D', False)],
        [('A', True), ('B', False), ('C', True), ('D', False)],
        [('A', False), ('B', False), ('C', False), ('D', True)],
    ]
    computed_values = evaluate_expression(test_data)
    print(computed_values)