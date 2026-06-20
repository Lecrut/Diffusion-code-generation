def xor_truth_table():
    for p in (True, False):
        for q in (True, False):
            yield p, q, p ^ q

if __name__ == '__main__':
    result = xor_truth_table()
    for p, q, r in result:
        print(f"P={p}, Q={q} => P XOR Q = {r}")