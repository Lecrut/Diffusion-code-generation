TRUE_VAL = True
FALSE_VAL = False

def evaluate_logic_sets(input_data):
    evaluated_results = []
    for current_set in input_data:
        lookup = dict(current_set)
        var_a = lookup.get('A', FALSE_VAL)
        var_b = lookup.get('B', FALSE_VAL)
        var_c = lookup.get('C', FALSE_VAL)
        var_d = lookup.get('D', FALSE_VAL)
        
        first_part = var_a and var_b
        second_part = var_c and (not var_d)
        
        final_value = first_part or second_part
        evaluated_results.append(final_value)
    return evaluated_results

if __name__ == '__main__':
    test_inputs = [
        [('A', True), ('B', True), ('C', True), ('D', False)],
        [('A', False), ('B', False), ('C', False), ('D', True)],
        [('A', True), ('B', False), ('C', False), ('D', False)],
        [('A', False), ('B', True), ('C', True), ('D', True)],
    ]
    output = evaluate_logic_sets(test_inputs)
    print(output)