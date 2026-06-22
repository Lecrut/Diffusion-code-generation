def compute_nand_result(a, b, c, d):
    return not (a and b and c and d)

def generate_truth_table():
    inputs = ['A', 'B', 'C', 'D']
    print(' | '.join(f'{h:<5}' for h in inputs + ['Result']))
    print('-' * 27)
    for i in range(16):
        val_d = (i >> 0) & 1
        val_c = (i >> 1) & 1
        val_b = (i >> 2) & 1
        val_a = (i >> 3) & 1
        bool_a = bool(val_a)
        bool_b = bool(val_b)
        bool_c = bool(val_c)
        bool_d = bool(val_d)
        res = compute_nand_result(bool_a, bool_b, bool_c, bool_d)
        row = [str(val_a), str(val_b), str(val_c), str(val_d), str(res)]
        print(' | '.join(f'{v:<5}' for v in row))

if __name__ == '__main__':
    generate_truth_table()