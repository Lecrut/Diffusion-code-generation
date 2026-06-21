def generate_truth_table(input_labels):
    if not input_labels:
        return
    num_vars = len(input_labels)
    total_combinations = 1 << num_vars
    column_width = max(len(label) for label in input_labels)
    separator = " | "
    header_parts = [label.center(column_width) for label in input_labels]
    header_line = separator.join(header_parts)
    print(header_line)
    separator_line = separator.join("-" * column_width)
    print(separator_line)
    for row_index in range(total_combinations):
        row_bits = []
        for col_index in range(num_vars):
            power = num_vars - 1 - col_index
            is_set = (row_index >> power) & 1
            row_bits.append(str(bool(is_set)))
        row_parts = [val.center(column_width) for val in row_bits]
        print(separator.join(row_parts))

if __name__ == '__main__':
    test_inputs = ["X", "Y", "Z"]
    generate_truth_table(test_inputs)