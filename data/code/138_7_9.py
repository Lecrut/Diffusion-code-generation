def xor_truth_table():
    for p in [True, False]:
        for q in [True, False]:
            yield (p, q, p ^ q)

if __name__ == '__main__':
    table = xor_truth_table()
    for row in table:
        print(f"P={row[0]}, Q={row[1]} => P XOR Q = {row[2]}")