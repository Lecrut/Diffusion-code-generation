def evaluate_expression(input_list):
    results = []
    for record in input_list:
        var_map = dict(record)
        val_a = var_map.get('A', False)
        val_b = var_map.get('B', False)
        val_c = var_map.get('C', False)
        val_d = var_map.get('D', False)
        first_part = val_a and val_b
        if first_part:
            results.append(True)
            continue
        second_part = val_c and not val_d
        results.append(second_part)
    return results

if __name__ == '__main__':
    test_cases = [
        [('A', True), ('B', True), ('C', False), ('D', False)],
        [('A', False), ('B', True), ('C', False), ('D', False)],
        [('A', False), ('B', False), ('C', True), ('D', False)],
        [('A', False), ('B', False), ('C', True), ('D', True)],
    ]
    output = evaluate_expression(test_cases)
    print(output)