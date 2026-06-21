def compute_logic_table():
    input_labels = ['A', 'B', 'C', 'D']
    num_inputs = len(input_labels)
    total_rows = 1 << num_inputs
    header = ' | '.join(f'{lbl:^5}' for lbl in input_labels + ['Result'])
    print(header)
    print('-' * len(header))
    for row_idx in range(total_rows):
        values = []
        for bit_pos in range(num_inputs):
            bit_val = (row_idx >> (num_inputs - 1 - bit_pos)) & 1
            values.append(bool(bit_val))
        A, B, C, D = values
        result = (A and B) or (not C and D)
        row_str = ' | '.join(f'{str(v):^5}' for v in values + [result])
        print(row_str)

if __name__ == '__main__':
    compute_logic_table()