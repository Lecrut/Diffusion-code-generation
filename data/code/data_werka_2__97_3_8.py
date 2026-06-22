def implication(p, q):
    if not isinstance(p, bool) or not isinstance(q, bool):
        raise ValueError("Inputs must be boolean")
    return (not p) or q

def generate_implication_table():
    values = [False, True]
    table = []
    for p in values:
        for q in values:
            res = implication(p, q)
            table.append((p, q, res))
    return table

def format_row(p, q, r):
    return f"P={p}, Q={q}, P -> Q={r}"

if __name__ == '__main__':
    table = generate_implication_table()
    for p, q, r in table:
        print(format_row(p, q, r))