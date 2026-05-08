import itertools
def generate_truth_table(inputs):
    num_inputs = len(inputs)
    num_rows = 2**num_inputs
    truth_table = []
    for i in range(num_rows):
        binary_representation = format(i, f'0{num_inputs}b')
        input_values = [int(bit) for bit in binary_representation]
        row = [input_values]
        for input_tuple in itertools.product([0, 1], repeat=num_inputs):
            row.append(list(input_tuple))
        truth_table.append(row)
    return truth_table
if __name__ == '__main__':
    sample_inputs = [True, False]
    truth_table_data = generate_truth_table(sample_inputs)
    header = list(sample_inputs)
    print("Inputs | Output")
    print("-" * 20)
    for row in truth_table_data:
        input_str = " | ".join(str(x) for x in row[0])
        output_str = " | ".join(str(x) for x in row[1:])
        print(f"{input_str} | {output_str}")