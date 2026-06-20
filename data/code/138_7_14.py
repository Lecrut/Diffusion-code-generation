def xor_truth_table_generator():
    for p in [True, False]:
        for q in [True, False]:
            yield (p, q, p != q)

if __name__ == '__main__':
    table = xor_truth_table_generator()
    for p, q, r in table:
        print(f"P={p}, Q={q} => P XOR Q = {r}")