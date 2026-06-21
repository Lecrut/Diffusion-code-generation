def generate_truth_table(variable_names):
    if not variable_names:
        return [], []
    count = len(variable_names)
    total_combinations = 1 << count
    header = list(variable_names)
    matrix = []
    for combination_index in range(total_combinations):
        current_row = []
        for position in range(count):
            mask = 1 << (count - 1 - position)
            is_set = bool(combination_index & mask)
            current_row.append(is_set)
        matrix.append(current_row)
    return header, matrix

if __name__ == '__main__':
    names = ['x', 'y', 'z']
    headers, table_data = generate_truth_table(names)
    print(headers)
    print(table_data)