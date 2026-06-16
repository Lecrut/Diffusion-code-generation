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
    c = 7.0 + 0.0j
    d = -3.0 - 4.0j
    e = 1.0 + 1.0j
    print(f"Comparing |{a}| and |{b}|: {compare_magnitudes(a, b)}")
    print(f"Comparing |{c}| and |{d}|: {compare_magnitudes(c, d)}")
    print(f"Comparing |{e}| and |{a}|: {compare_magnitudes(e, a)}")
    z1 = 1.0 + 2.0j
    z2 = 1.0000000000000001 + 2.0j
    print(f"Comparing |{z1}| and |{z2}| (close): {compare_magnitudes(z1, z2)}")
    z3 = 5.0 + 0.0j
    z4 = -5.0 + 0.0j
    print(f"Comparing |{z3}| and |{z4}|: {compare_magnitudes(z3, z4)}")