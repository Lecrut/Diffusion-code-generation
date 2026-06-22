def generate_truth_table():
    rows = []
    for p in [False, True]:
        for q in [False, True]:
            implication = (not p) or q
            rows.append((p, q, implication))
    return rows

if __name__ == '__main__':
    table = generate_truth_table()
    print(f"P\tQ\tP -> Q")
    print("-" * 20)
    for p, q, res in table:
        print(f"{str(p)}\t{str(q)}\t{str(res)}")