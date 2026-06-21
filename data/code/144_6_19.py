def nand(a, b):
    return not (a and b)

def generate_truth_table():
    truth_table = {}
    inputs = [False, True]
    for a in inputs:
        for b in inputs:
            truth_table[(a, b)] = nand(a, b)
    return truth_table

if __name__ == '__main__':
    print(generate_truth_table())