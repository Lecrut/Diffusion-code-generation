def is_zero(val): return val == 0 if isinstance(val, (int, float)) else False

if __name__ == '__main__':
    samples = [0, -1e-256, 42, "zero", True]
    for s in samples:
        print(f"{s!r}: {is_zero(s)}")