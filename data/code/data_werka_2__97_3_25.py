def generate_truth_table():
    rows = []
    for p in [True, False]:
        for q in [True, False]:
            result = (not p) or q
            rows.append((p, q, result))
    return rows

if __name__ == '__main__':
    table = generate_truth_table()
    for p, q, r in table:
        print(f"P={p}, Q={q}, P -> Q={r}")