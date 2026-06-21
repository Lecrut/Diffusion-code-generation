def generate_truth_table(inputs):
    NUM_INPUTS = len(inputs)
    TOTAL_ROWS = 1 << NUM_INPUTS
    SEPARATOR = " | "
    HEADER = SEPARATOR.join(inputs)
    DIVIDER = "-" * len(HEADER)
    
    print(HEADER)
    print(DIVIDER)
    
    for row_index in range(TOTAL_ROWS):
        row_bits = []
        for col_index in range(NUM_INPUTS):
            bit_position = NUM_INPUTS - 1 - col_index
            bit_value = (row_index >> bit_position) & 1
            row_bits.append(str(bool(bit_value)))
        print(SEPARATOR.join(row_bits))

if __name__ == '__main__':
    generate_truth_table(["X", "Y", "Z"])