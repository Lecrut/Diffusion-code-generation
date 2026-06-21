def nand_operation(a, b):
    return not (a and b)

def generate_truth_table(operation):
    truth_table = {}
    for a in [False, True]:
        for b in [False, True]:
            result = operation(a, b)
            truth_table[(a, b)] = result
    return truth_table

if __name__ == '__main__':
    sample_inputs = [(True, False), (False, True), (True, True), (False, False)]
    nand_truth_table = generate_truth_table(nand_operation)
    for inputs in sample_inputs:
        print(f"Input: {inputs} Output: {nand_truth_table[inputs]}")