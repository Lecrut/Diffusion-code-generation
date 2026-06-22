def generate_truth_table():
    rows = []
    for p in [False, True]:
        for q in [False, True]:
            implication = (not p) or q
            rows.append((p, q, implication))
    return rows

if __name__ == '__main__':
    table = generate_truth_table()
    for p, q, r in table:
        print(f"P={p}, Q={q}, P -> Q={r}")