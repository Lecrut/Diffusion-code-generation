def generate_truth_table(input_vars):
    num_vars = len(input_vars)
    num_rows = 2 ** num_vars
    if num_vars == 0:
        num_rows = 1
    header = [f"Input {i+1}" for i in range(num_vars)]
    header.append("Output")
    print(" | ".join(header))
    print("-" * (len(" | ".join(header)) + 3))
    for i in range(num_rows):
        input_combination = []
        for j in range(num_vars):
            bit = (i >> j) & 1
            input_combination.append(str(bit))
        input_str = " ".join(input_combination)
        output_value = ""
        if num_vars == 1:
            output_value = str(input_vars[0])
        else:
            output_value = "".join(input_combination)
        print(f"{input_str} | {output_value}")
if __name__ == '__main__':
    sample_inputs_2 = [False, True]
    print("Truth Table for 2 Variables:")
    generate_truth_table(sample_inputs_2)
    print("\n" + "="*30 + "\n")
    sample_inputs_3 = [False, True, False]
    print("Truth Table for 3 Variables:")
    generate_truth_table(sample_inputs_3)