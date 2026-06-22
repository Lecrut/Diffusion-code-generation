def truth_table():
    results = []
    for p in (False, True):
        for q in (False, True):
            val = (not p) or q
            results.append((p, q, val))
    return results

def display(table):
    for p, q, r in table:
        print(f"P={p}, Q={q}, P -> Q={r}")

if __name__ == '__main__':
    t = truth_table()
    display(t)