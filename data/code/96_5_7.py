def evaluate_expression(input_set):
    variable_map = {
        'A': False,
        'B': False,
        'C': False,
        'D': False,
    }
    for key, value in input_set:
        if key in variable_map:
            variable_map[key] = value
    a_val = variable_map['A']
    b_val = variable_map['B']
    c_val = variable_map['C']
    d_val = variable_map['D']
    first_part = a_val and b_val
    second_part = c_val and (not d_val)
    final_result = first_part or second_part
    return final_result

if __name__ == '__main__':
    test_cases = [
        [('A', True), ('B', False), ('C', False), ('D', True)],
        [('A', False), ('B', False), ('C', True), ('D', False)],
        [('A', True), ('B', True), ('C', False), ('D', False)],
        [('A', False), ('B', True), ('C', False), ('D', True)],
    ]
    outcomes = [evaluate_expression(tc) for tc in test_cases]
    print(outcomes)