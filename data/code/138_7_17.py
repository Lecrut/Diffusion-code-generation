def xor_truth_table():
    for p in (False, True):
        for q in (False, True):
            yield (p, q, p ^ q)

if __name__ == '__main__':
    sample_p = False
    sample_q = True
    print(f"P={sample_p}, Q={sample_q} => P ^ Q =", xor_truth_table().__next__()[2])