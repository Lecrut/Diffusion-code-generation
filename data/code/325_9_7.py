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
    b = 5.0 - 12.0j
    c = 7.0 + 0.0j
    d = 1.0 + 1.0j
    print(f"Comparing magnitude of {a} and {b}: {compare_magnitudes(a, b)}")
    print(f"Comparing magnitude of {a} and {c}: {compare_magnitudes(a, c)}")
    print(f"Comparing magnitude of {d} and {a}: {compare_magnitudes(d, a)}")
    e = 1.0 + 1.0j * (1.0 + 1.0)
    f = 2.0 + 2.0j
    print(f"Comparing magnitude of {e} and {f}: {compare_magnitudes(e, f)}")