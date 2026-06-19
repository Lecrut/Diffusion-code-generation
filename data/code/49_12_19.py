import math

EPSILON = 1e-9

def compare_lengths(length1, length2):
    if math.isclose(length1, length2, abs_tol=EPSILON):
        return "Both lengths are equal"
    elif length1 > length2:
        return length1
    else:
        return length2

if __name__ == '__main__':
    length_a = 10.00000001
    length_b = 10.0
    result = compare_lengths(length_a, length_b)
    print(f"Result of comparison: {result}")

    length_c = 5.99999999
    length_d = 6.0
    result2 = compare_lengths(length_c, length_d)
    print(f"Result of second comparison: {result2}")