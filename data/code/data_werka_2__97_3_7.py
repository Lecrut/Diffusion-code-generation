def compute_implication(p, q):
    return (not p) or q

def build_truth_table():
    values = [False, True]
    table = []
    for p in values:
        for q in values:
            result = compute_implication(p, q)
            table.append((p, q, result))
    return table

def print_table(table):
    for p, q, impl in table:
        print(f"P={p}, Q={q}, P -> Q={impl}")

if __name__ == '__main__':
    table = build_truth_table()
    print_table(table)