from itertools import product

OR_MAP = {
    (False, False): False,
    (False, True): True,
    (True, False): True,
    (True, True): True,
}

def compute_or_truth_table(num_vars=2):
    rows = []
    for vals in product([False, True], repeat=num_vars):
        result = OR_MAP[vals]
        rows.append(list(vals) + [result])
    return rows

if __name__ == '__main__':
    table = compute_or_truth_table()
    print(table)