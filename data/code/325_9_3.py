import math
def compare_magnitudes(z1, z2, tolerance=1e-9):
    mag1 = abs(z1)
    mag2 = abs(z2)
    if abs(mag1 - mag2) < tolerance:
        return 0
    elif mag1 < mag2:
        return -1
    else:
        return 1
if __name__ == '__main__':
    a = 3.0 + 4.0j
    b = 5.0 + 12.0j
    c = 3.000000000000001 + 4.0j
    d = 3.0 + 4.0j
    print(f"Comparing magnitude of {a} and {b}: {compare_magnitudes(a, b)}")
    print(f"Comparing magnitude of {a} and {c}: {compare_magnitudes(a, c)}")
    print(f"Comparing magnitude of {a} and {d}: {compare_magnitudes(a, d)}")
    e = 1.0 + 1.0j
    f = 1.0000000000000002 + 1.0j
    print(f"Comparing magnitude of {e} and {f}: {compare_magnitudes(e, f)}")