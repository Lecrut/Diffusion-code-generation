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
            output_tuple = []
            for input_val in input_tuple:
                result = 0
                for input_index in range(num_inputs):
                    if input_val == 1:
                        result ^= inputs[input_index]
                output_tuple.append(result)
            truth_table.append(output_tuple)
    return truth_table
if __name__ == '__main__':
    sample_inputs = [0, 1, 1]
    truth_table_data = generate_truth_table(sample_inputs)
    print("Inputs:", sample_inputs)
    print("Truth Table:")
    header = " | ".join(map(str, sample_inputs))
    print(f"{'Output':<10} | {header}")
    for row in truth_table_data:
        print(f"{row[0]:<10} |", end="")
        for val in row[1:]:
            print(f"{val:2}", end="")
        print()