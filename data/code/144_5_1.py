def generate_truth_table(input_booleans):
    n = len(input_booleans)
    num_rows = 2**n
    truth_table = []
    for i in range(num_rows):
        row = []
        for j in range(n):
            bit = (i >> j) & 1
            row.append(input_booleans[j])
        truth_table.append(row)
    return truth_table
if __name__ == '__main__':
    sample_inputs = [False, True]
    result = generate_truth_table(sample_inputs)
    print(result)