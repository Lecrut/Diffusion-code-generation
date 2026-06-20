def xor_truth_table_generator():
    for p in [True, False]:
        for q in [True, False]:
            yield (p, q, p ^ q)

if __name__ == '__main__':
    truth_table_gen = xor_truth_table_generator()
    for row in truth_table_gen:
        print(f"P={row[0]}, Q={row[1]} => P ^ Q = {row[2]}")