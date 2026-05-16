import math
def simplify_ratio(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    if numerator == 0:
        return 0, 1
    common_divisor = math.gcd(abs(numerator), abs(denominator))
    simplified_numerator = numerator // common_divisor
    simplified_denominator = denominator // common_divisor
    if simplified_denominator < 0:
        simplified_numerator = -simplified_numerator
        simplified_denominator = -simplified_denominator
    return simplified_numerator, simplified_denominator
def calculate_ratio(a, b):
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    return a / b
def find_greatest_common_divisor(a, b):
    return math.gcd(a, b)
def reduce_to_simplest_fraction(num, den):
    if den == 0:
        raise ValueError("Denominator cannot be zero")
    if num == 0:
        return 0, 1
    common = find_greatest_common_divisor(abs(num), abs(den))
    new_num = num // common
    new_den = den // common
    if new_den < 0:
        new_num = -new_num
        new_den = -new_den
    return new_num, new_den
if __name__ == '__main__':
    print("--- Testing simplify_ratio ---")
    n1, d1 = 12, 18
    s1, r1 = simplify_ratio(n1, d1)
    print(f"Ratio {n1}/{d1} simplified to: {s1}/{r1}")
    n2, d2 = -20, 40
    s2, r2 = simplify_ratio(n2, d2)
    print(f"Ratio {n2}/{d2} simplified to: {s2}/{r2}")
    n3, d3 = 100, 50
    s3, r3 = simplify_ratio(n3, d3)
    print(f"Ratio {n3}/{d3} simplified to: {s3}/{r3}")
    print("\n--- Testing calculate_ratio ---")
    a4, b4 = 10, 4
    ratio4 = calculate_ratio(a4, b4)
    print(f"Ratio {a4}/{b4} is: {ratio4}")
    a5, b5 = -15, 5
    ratio5 = calculate_ratio(a5, b5)
    print(f"Ratio {a5}/{b5} is: {ratio5}")
    print("\n--- Testing find_greatest_common_divisor ---")
    a6, b6 = 48, 18
    gcd6 = find_greatest_common_divisor(a6, b6)
    print(f"GCD of {a6} and {b6} is: {gcd6}")
    a7, b7 = 101, 103
    gcd7 = find_greatest_common_divisor(a7, b7)
    print(f"GCD of {a7} and {b7} is: {gcd7}")
    print("\n--- Testing reduce_to_simplest_fraction ---")
    n8, d8 = 36, 12
    s8, r8 = reduce_to_simplest_fraction(n8, d8)
    print(f"Fraction {n8}/{d8} reduced to: {s8}/{r8}")
    n9, d9 = -30, 60
    s9, r9 = reduce_to_simplest_fraction(n9, d9)
    print(f"Fraction {n9}/{d9} reduced to: {s9}/{r9}")
    n10, d10 = 10, -20
    s10, r10 = reduce_to_simplest_fraction(n10, d10)
    print(f"Fraction {n10}/{d10} reduced to: {s10}/{r10}")