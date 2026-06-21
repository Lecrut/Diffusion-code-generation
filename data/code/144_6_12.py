def nand_operation(a, b):
    return not (a and b)

def generate_truth_table():
    truth_table = {}
    for a in [False, True]:
        for b in [False, True]:
            truth_table[(a, b)] = nand_operation(a, b)
    return truth_table

if __name__ == '__main__':
    truth_table = generate_truth_table()
    print(truth_table)