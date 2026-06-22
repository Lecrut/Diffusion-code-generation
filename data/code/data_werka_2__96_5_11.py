def evaluate_expression(input_list):
    if not input_list:
        return []
    required_keys = {'A', 'B', 'C', 'D'}
    results = []
    for record in input_list:
        if not isinstance(record, (list, tuple)):
            raise ValueError("Each input set must be a list or tuple of tuples.")
        var_dict = dict(record)
        missing = required_keys - set(var_dict.keys())
        if missing:
            raise ValueError(f"Missing variables: {missing}")
        for key in required_keys:
            val = var_dict[key]
            if not isinstance(val, bool):
                raise ValueError(f"Variable {key} must be a boolean, got {type(val).__name__}")
        A = var_dict['A']
        B = var_dict['B']
        C = var_dict['C']
        D = var_dict['D']
        term_left = A and B
        term_right = C and (not D)
        final_val = term_left or term_right
        results.append(final_val)
    return results

if __name__ == '__main__':
    sample_data = [
        [('A', True), ('B', True), ('C', False), ('D', False)],
        [('A', False), ('B', False), ('C', True), ('D', True)],
        [('A', True), ('B', False), ('C', True), ('D', False)],
        [('A', False), ('B', True), ('C', False), ('D', True)],
        [('A', True), ('B', True), ('C', True), ('D', True)],
    ]
    computed_results = evaluate_expression(sample_data)
    print(computed_results)