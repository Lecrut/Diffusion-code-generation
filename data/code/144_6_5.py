def nand_operation(a, b):
    return not (a and b)

def generate_truth_table():
    truth_table = {}
    inputs = [(False, False), (False, True), (True, False), (True, True)]
    for a, b in inputs:
        truth_table[(a, b)] = nand_operation(a, b)
    return truth_table

if __name__ == '__main__':
    sample_truth_table = generate_truth_table()
    print(sample_truth_table)