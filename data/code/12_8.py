import math
def simplify_ratio(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    common = math.gcd(numerator, denominator)
    return numerator // common, denominator // common
def calculate_ratio(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a / b
def find_ratio_of_two_numbers(num1, num2):
    if num2 == 0:
        raise ValueError("Second number cannot be zero")
    return num1 / num2
def ratio_to_fraction(ratio):
    if ratio == 0:
        return 0, 1
    numerator = int(ratio)
    denominator = 1
    if ratio != int(ratio):
        numerator = int(ratio * 1000000)
        denominator = 1000000
    return numerator, denominator
if __name__ == '__main__':
    print("--- Testing simplify_ratio ---")
    n1, d1 = 12, 18
    s1, d2 = simplify_ratio(n1, d1)
    print(f"Simplifying {n1}/{d1}: {n1}/{d1} -> {s1}/{d2}")
    n3, d3 = 100, 75
    s2, d4 = simplify_ratio(n3, d3)
    print(f"Simplifying {n3}/{d3}: {n3}/{d3} -> {s2}/{d4}")
    n5, d5 = 17, 34
    s3, d6 = simplify_ratio(n5, d5)
    print(f"Simplifying {n5}/{d5}: {n5}/{d5} -> {s3}/{d6}")
    print("\n--- Testing calculate_ratio ---")
    a = 10
    b = 4
    r1 = calculate_ratio(a, b)
    print(f"Ratio of {a} to {b}: {a}/{b} = {r1}")
    a = 5
    b = 0
    try:
        r2 = calculate_ratio(a, b)
    except ValueError as e:
        print(f"Error calculating ratio of {a} to {b}: {e}")
    print("\n--- Testing find_ratio_of_two_numbers ---")
    num1 = 20
    num2 = 5
    r3 = find_ratio_of_two_numbers(num1, num2)
    print(f"Ratio of {num1} to {num2}: {num1}/{num2} = {r3}")
    num1 = 15
    num2 = 4
    r4 = find_ratio_of_two_numbers(num1, num2)
    print(f"Ratio of {num1} to {num2}: {num1}/{num2} = {r4}")
    print("\n--- Testing ratio_to_fraction ---")
    ratio1 = 1.5
    n1_f, d1_f = ratio_to_fraction(ratio1)
    print(f"Ratio {ratio1} converted to fraction: {n1_f}/{d1_f}")
    ratio2 = 3.0
    n2_f, d2_f = ratio_to_fraction(ratio2)
    print(f"Ratio {ratio2} converted to fraction: {n2_f}/{d2_f}")
    ratio3 = 1.2345
    n3_f, d3_f = ratio_to_fraction(ratio3)
    print(f"Ratio {ratio3} converted to fraction (scaled): {n3_f}/{d3_f}")