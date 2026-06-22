def generate_implication_truth_table():
    rows = []
    for p in [False, True]:
        for q in [False, True]:
            result = (not p) or q
            rows.append((p, q, result))
    return rows

def print_truth_table(table):
    print("P\tQ\tP -> Q")
    print("-" * 15)
    for p, q, r in table:
        p_str = str(p)
        q_str = str(q)
        r_str = str(r)
        print(f"{p_str}\t{q_str}\t{r_str}")

if __name__ == '__main__':
    table = generate_implication_truth_table()
    print_truth_table(table)