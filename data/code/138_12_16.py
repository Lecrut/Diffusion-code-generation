def generate_truth_table(expression):
    if not isinstance(expression, str) or len(expression) == 0:
        return "Error: Input must be a non-empty string representing a boolean expression."

    inputs = ['a', 'b'] if 'b' in expression else ['a']
    num_inputs = len(inputs)
    num_rows = 2 ** num_inputs

    table = []
    for i in range(num_rows):
        row = {}
        for j, input_var in enumerate(inputs):
            if (i >> j) & 1:
                row[input_var] = True
            else:
                row[input_var] = False
        row['result'] = eval(expression, {}, row)
        table.append(row)

    return table

if __name__ == '__main__':
    sample_expression_1 = "a and b"
    print(generate_truth_table(sample_expression_1))

    sample_expression_2 = "not a or b"
    print(generate_truth_table(sample_expression_2))