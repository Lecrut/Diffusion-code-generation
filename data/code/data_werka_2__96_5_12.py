def evaluate_boolean_expression(input_tuples):
    var_lookup = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    results = []
    for record in input_tuples:
        values = dict(record)
        val_a = values.get('A', False)
        val_b = values.get('B', False)
        val_c = values.get('C', False)
        val_d = values.get('D', False)
        term_one = val_a and val_b
        term_two = val_c and (not val_d)
        combined = term_one or term_two
        results.append(combined)
    return results

if __name__ == '__main__':
    test_data = [
        [('A', True), ('B', True), ('C', False), ('D', False)],
        [('A', False), ('B', False), ('C', True), ('D', True)],
        [('A', True), ('B', False), ('C', True), ('D', False)],
        [('A', False), ('B', True), ('C', False), ('D', True)],
        [('A', True), ('B', True), ('C', True), ('D', True)],
    ]
    output = evaluate_boolean_expression(test_data)
    print(output)