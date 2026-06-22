def compute_or_table(combinations):
    table_rows = []
    for input_pair in combinations:
        left_val = input_pair[0]
        right_val = input_pair[1]
        logical_result = left_val or right_val
        row_entry = [left_val, right_val, logical_result]
        table_rows.append(row_entry)
    return table_rows

if __name__ == '__main__':
    test_inputs = [[True, True], [False, False], [True, False], [False, True]]
    final_table = compute_or_table(test_inputs)
    print(final_table)