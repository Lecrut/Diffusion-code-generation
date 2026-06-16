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
    d = 3.0 + 4.000000000000001j
    result1 = compare_magnitudes(a, b)
    print(f"Comparison of |{a}| and |{b}|: {result1}")
    result2 = compare_magnitudes(a, c)
    print(f"Comparison of |{a}| and |{c}|: {result2}")
    result3 = compare_magnitudes(a, d)
    print(f"Comparison of |{a}| and |{d}| (testing tolerance): {result3}")
    e = 1.0 + 1.0j
    f = 1.0000000000000002 + 1.0j
    result4 = compare_magnitudes(e, f)
    print(f"Comparison of |{e}| and |{f}| (testing tolerance): {result4}")