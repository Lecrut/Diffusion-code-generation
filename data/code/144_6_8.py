NAND_OUTPUT = {False: True, True: False}

def nand_operation(a, b):
    return NAND_OUTPUT[a != b]

def generate_truth_table():
    truth_table = {}
    for a in [False, True]:
        for b in [False, True]:
            truth_table[(a, b)] = nand_operation(a, b)
    return truth_table

if __name__ == '__main__':
    print(generate_truth_table())