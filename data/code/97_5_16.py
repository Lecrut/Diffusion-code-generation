def create_truth_table():
    NUM_INPUTS = 4
    INPUT_NAMES = ['A', 'B', 'C', 'D']
    NUM_ROWS = 1 << NUM_INPUTS
    HEADER_SEP = " | "
    SEPARATOR_LEN = 30
    TRUTH_VALS = [False, True]

    def compute_expression(a, b, c, d):
        return (a and b) or (c and d)

    def format_row(values):
        parts = [str(v) for v in values]
        return HEADER_SEP.join(parts)

    def generate_rows():
        rows = []
        for row_index in range(NUM_ROWS):
            current_inputs = []
            for input_index in range(NUM_INPUTS):
                bit_mask = NUM_ROWS >> (input_index + 1)
                is_set = (row_index & bit_mask) != 0
                current_inputs.append(is_set)
            result = compute_expression(*current_inputs)
            row_values = current_inputs + [result]
            rows.append(format_row(row_values))
        return rows

    headers = INPUT_NAMES + ['Result']
    header_line = HEADER_SEP.join(f"{h:<10}" for h in headers)
    separator_line = "-" * SEPARATOR_LEN

    table_lines = [header_line, separator_line]
    table_lines.extend(generate_rows())
    
    return "\n".join(table_lines)

if __name__ == '__main__':
    output = create_truth_table()
    print(output)