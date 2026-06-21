def generate_truth_table():
    rows = []
    for p in [False, True]:
        for q in [False, True]:
            implication = (not p) or q
            rows.append((p, q, implication))
    return rows

def print_truth_table(table):
    print("P\tQ\tP -> Q")
    print("-\t-\t------")
    for p, q, impl in table:
        p_str = "T" if p else "F"
        q_str = "T" if q else "F"
        impl_str = "T" if impl else "F"
        print(f"{p_str}\t{q_str}\t{impl_str}")

if __name__ == '__main__':
    table = generate_truth_table()
    print_truth_table(table)