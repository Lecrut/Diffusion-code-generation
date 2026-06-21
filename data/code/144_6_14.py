def nand_operation(a, b):
    return not (a and b)

def generate_truth_table(rule):
    truth_table = {}
    for a in [False, True]:
        for b in [False, True]:
            truth_table[(a, b)] = rule(a, b)
    return truth_table

if __name__ == '__main__':
    nand_table = generate_truth_table(nand_operation)
    print(nand_table)