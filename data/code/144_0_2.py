import itertools
def generate_truth_table(inputs):
    num_inputs = len(inputs)
    num_rows = 2**num_inputs
    truth_table = []
    for i in range(num_rows):
        input_values = []
        temp = i
        for _ in range(num_inputs):
            input_values.append(temp % 2)
            temp //= 2
        input_values.reverse()
        output = []
        for input_tuple in itertools.product([0, 1], repeat=num_inputs):
            result = 0
            for j in range(num_inputs):
                if input_tuple[j] == 1:
                    result |= inputs[j]
            output.append(result)
        truth_table.append(input_values + output)
    return truth_table
if __name__ == '__main__':
    sample_inputs = [False, True]
    truth_table_data = generate_truth_table(sample_inputs)
    print("Inputs: False, True")
    print("--------------------")
    print("Input | Output")
    print("--------------------")
    for row in truth_table_data:
        input_str = " | ".join(map(str, row[:len(sample_inputs)]))
        output_str = " | ".join(map(str, row[len(sample_inputs):]))
        print(f"{input_str} | {output_str}")