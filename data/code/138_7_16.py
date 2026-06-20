XOR_TABLE = [(False, False), (False, True), (True, False), (True, True)]

def xor_truth_table():
    for p, q in XOR_TABLE:
        yield (p, q, p != q)

if __name__ == '__main__':
    for p, q, r in xor_truth_table():
        print(f"P={p}, Q={q} => P ^ Q = {r}")