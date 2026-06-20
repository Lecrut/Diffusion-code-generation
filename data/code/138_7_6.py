def xor_generator():
    yield (False, False, False)
    yield (False, True, True)
    yield (True, False, True)
    yield (True, True, False)

if __name__ == '__main__':
    for p, q, r in xor_generator():
        print(f"P={p}, Q={q} => P ^ Q = {r}")