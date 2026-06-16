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
    d = 10.0 + 0.0j
    print(f"Comparing |{a}| and |{b}|:")
    result1 = compare_magnitudes(a, b)
    print(f"Result: {result1}")
    print(f"\nComparing |{c}| and |{d}|:")
    result2 = compare_magnitudes(c, d)
    print(f"Result: {result2}")
    print(f"\nComparing |{a}| and |{c}|:")
    result3 = compare_magnitudes(a, c)
    print(f"Result: {result3}")