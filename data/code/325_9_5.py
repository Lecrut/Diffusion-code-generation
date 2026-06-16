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
    d = 1.0 + 0.0j
    print(f"Comparing magnitude of {a}: {abs(a)}")
    print(f"Comparing magnitude of {b}: {abs(b)}")
    print(f"Comparing magnitude of {c}: {abs(c)}")
    print(f"Comparing magnitude of {d}: {abs(d)}")
    result1 = compare_magnitudes(a, b)
    print(f"Comparison between a and b (mag): {result1}")
    result2 = compare_magnitudes(a, c)
    print(f"Comparison between a and c (mag): {result2}")
    result3 = compare_magnitudes(b, d)
    print(f"Comparison between b and d (mag): {result3}")
    e = 1.0 + 1.0j * (1.0 + 1.0)
    f = 2.0 + 2.0j
    print(f"\nComparing magnitude of {e}: {abs(e)}")
    print(f"Comparing magnitude of {f}: {abs(f)}")
    result4 = compare_magnitudes(e, f)
    print(f"Comparison between e and f (mag): {result4}")