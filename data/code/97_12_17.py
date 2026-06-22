from itertools import product

def compute_xor_table():
    rows = []
    for a, b in product((0, 1), repeat=2):
        rows.append((a, b, a ^ b))
    return rows

if __name__ == '__main__':
    truth_table = compute_xor_table()
    print(truth_table)