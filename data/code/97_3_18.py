def generate_implication_truth_table():
    rows = []
    for p in [False, True]:
        for q in [False, True]:
            result = (not p) or q
            rows.append((p, q, result))
    return rows

if __name__ == '__main__':
    table = generate_implication_truth_table()
    print("P\tQ\tP -> Q")
    print("-\t-\t------")
    for p, q, res in table:
        print(f"{p}\t{q}\t{res}")