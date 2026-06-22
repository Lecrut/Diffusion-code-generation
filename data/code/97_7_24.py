def generate_truth_table(variables):
    num_vars = len(variables)
    total_rows = 1 << num_vars
    rows = []
    for row_index in range(total_rows):
        row_values = []
        for var_index in range(num_vars):
            bit_position = num_vars - 1 - var_index
            is_set = (row_index >> bit_position) & 1
            row_values.append(bool(is_set))
        rows.append(row_values)
    return variables, rows

if __name__ == '__main__':
    variable_names = ['P', 'Q', 'R']
    headers, table_rows = generate_truth_table(variable_names)
    print(headers)
    for row in table_rows:
        print(row)