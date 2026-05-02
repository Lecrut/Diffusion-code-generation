import math
def simplify_ratio(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    if numerator == 0:
        return 0, 1
    common = math.gcd(abs(numerator), abs(denominator))
    simplified_num = numerator // common
    simplified_den = denominator // common
    if simplified_den < 0:
        simplified_num = -simplified_num
        simplified_den = -simplified_den
    return simplified_num, simplified_den
def calculate_ratio(a, b):
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    return a / b
def find_greatest_common_divisor(a, b):
    return math.gcd(a, b)
def reduce_to_simplest_form(num, den):
    if den == 0:
        raise ValueError("Denominator cannot be zero")
    common = find_greatest_common_divisor(num, den)
    simplified_num = num // common
    simplified_den = den // common
    if simplified_den < 0:
        simplified_num = -simplified_num
        simplified_den = -simplified_den
    return simplified_num, simplified_den
if __name__ == '__main__':
    print("--- Testing simplify_ratio ---")
    num1, den1 = 12, 18
    print(f"Ratio {num1}/{den1}: Simplified to ({simplify_ratio(num1, den1)[0]}/{simplify_ratio(num1, den1)[1]})")
    num2, den2 = -20, 40
    print(f"Ratio {num2}/{den2}: Simplified to ({simplify_ratio(num2, den2)[0]}/{simplify_ratio(num2, den2)[1]})")
    num3, den3 = 7, 7
    print(f"Ratio {num3}/{den3}: Simplified to ({simplify_ratio(num3, den3)[0]}/{simplify_ratio(num3, den3)[1]})")
    num4, den4 = 100, 50
    print(f"Ratio {num4}/{den4}: Simplified to ({simplify_ratio(num4, den4)[0]}/{simplify_ratio(num4, den4)[1]})")
    print("\n--- Testing calculate_ratio ---")
    a = 10
    b = 5
    print(f"Ratio {a}/{b}: {calculate_ratio(a, b)}")
    a = 10
    b = -5
    print(f"Ratio {a}/{b}: {calculate_ratio(a, b)}")
    print("\n--- Testing find_greatest_common_divisor ---")
    a = 48
    b = 18
    print(f"GCD of {a} and {b}: {find_greatest_common_divisor(a, b)}")
    a = -30
    b = 42
    print(f"GCD of {a} and {b}: {find_greatest_common_divisor(a, b)}")
    print("\n--- Testing reduce_to_simplest_form ---")
    num5, den5 = 36, 54
    print(f"Ratio {num5}/{den5}: Reduced to ({reduce_to_simplest_form(num5, den5)[0]}/{reduce_to_simplest_form(num5, den5)[1]})")
    num6, den6 = -100, 25
    print(f"Ratio {num6}/{den6}: Reduced to ({reduce_to_simplest_form(num6, den6)[0]}/{reduce_to_simplest_form(num6, den6)[1]})")
    num7, den7 = 11, 22
    print(f"Ratio {num7}/{den7}: Reduced to ({reduce_to_simplest_form(num7, den7)[0]}/{reduce_to_simplest_form(num7, den7)[1]})")