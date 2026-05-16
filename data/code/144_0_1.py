import itertools
def generate_truth_table(inputs):
    num_inputs = len(inputs)
    num_rows = 2**num_inputs
    table = []
    for i in range(num_rows):
        row = [False] * num_inputs
        temp = i
        for j in range(num_inputs):
            row[j] = bool(temp & 1)
            temp >>= 1
        table.append(row)
    return table
if __name__ == '__main__':
    sample_inputs = [True, False]
    truth_table = generate_truth_table(sample_inputs)
    for row in truth_table:
        print(" ".join(map(str, row)))