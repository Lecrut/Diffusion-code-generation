def evaluate_expression(input_list):
    term_a = None
    term_b = None
    term_c = None
    term_d = None
    output_results = []
    for record in input_list:
        var_dict = dict(record)
        term_a = var_dict.get('A', False)
        term_b = var_dict.get('B', False)
        term_c = var_dict.get('C', False)
        term_d = var_dict.get('D', False)
        first_part = term_a and term_b
        second_part = term_c and (not term_d)
        combined = first_part or second_part
        output_results.append(combined)
    return output_results
if __name__ == '__main__':
    data_set = [
        [('A', True), ('B', False), ('C', True), ('D', True)],
        [('A', False), ('B', True), ('C', True), ('D', False)],
        [('A', True), ('B', True), ('C', False), ('D', False)],
        [('A', False), ('B', False), ('C', False), ('D', True)],
    ]
    print(evaluate_expression(data_set))