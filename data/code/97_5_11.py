TRUE_VAL = True
FALSE_VAL = False
INPUT_NAMES = ['A', 'B', 'C', 'D']
NUM_INPUTS = len(INPUT_NAMES)
TOTAL_ROWS = 1 << NUM_INPUTS

def compute_result(row_bits):
    a, b, c, d = row_bits
    return (a and b) or (c and d)

def generate_truth_table():
    header = ' | '.join(f'{name:<5}' for name in INPUT_NAMES) + ' | Result'
    print(header)
    print('-' * len(header))
    for i in range(TOTAL_ROWS):
        bits = []
        for j in range(NUM_INPUTS):
            bit_index = NUM_INPUTS - 1 - j
            val = (i >> bit_index) & 1
            bits.append(bool(val))
        result = compute_result(bits)
        row_str = ' | '.join(f'{str(b):<5}' for b in bits) + f' | {result}'
        print(row_str)

if __name__ == '__main__':
    generate_truth_table()