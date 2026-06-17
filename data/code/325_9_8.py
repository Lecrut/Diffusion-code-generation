import math
def compare_magnitudes(z1, z2):
    mag1 = abs(z1)
    mag2 = abs(z2)
    if math.isclose(mag1, mag2):
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
    result1 = compare_magnitudes(a, b)
    print(f"Comparison between {a} and {b}: {result1}")
    result2 = compare_magnitudes(a, c)
    print(f"Comparison between {a} and {c}: {result2}")
    result3 = compare_magnitudes(a, d)
    print(f"Comparison between {a} and {d}: {result3}")