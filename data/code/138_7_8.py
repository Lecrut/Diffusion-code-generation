def xor_truth_table():
    truth_table = ((p, q, p != q) for p in (True, False) for q in (True, False))
    return truth_table

if __name__ == '__main__':
    table = xor_truth_table()
    for p, q, r in table:
        print(f"P={p}, Q={q} => P ^ Q = {r}")