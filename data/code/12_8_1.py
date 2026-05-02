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
def reduce_to_fraction(ratio):
    if not isinstance(ratio, tuple) or len(ratio) != 2:
        raise TypeError("Input must be a tuple of two numbers (numerator, denominator)")
    numerator, denominator = ratio
    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    return simplify_ratio(numerator, denominator)
def calculate_ratio_difference(ratio1, ratio2):
    num1, den1 = reduce_to_fraction(ratio1)
    num2, den2 = reduce_to_fraction(ratio2)
    common_denominator = den1 * den2
    diff = (num1 * den2) - (num2 * den1)
    if diff == 0:
        return (0, 1)
    common_divisor = math.gcd(abs(diff), common_denominator)
    final_numerator = diff // common_divisor
    final_denominator = common_denominator // common_divisor
    if final_denominator < 0:
        final_numerator = -final_numerator
        final_denominator = -final_denominator
    return final_numerator, final_denominator
if __name__ == '__main__':
    ratio_a = (12, 18)
    ratio_b = (20, 30)
    ratio_c = (5, 7)
    ratio_d = (100, 50)
    ratio_e = (-15, 25)
    ratio_f = (10, 0)
    print(f"Simplifying {ratio_a}: {reduce_to_fraction(ratio_a)}")
    print(f"Simplifying {ratio_b}: {reduce_to_fraction(ratio_b)}")
    print(f"Simplifying {ratio_c}: {reduce_to_fraction(ratio_c)}")
    print(f"Simplifying {ratio_d}: {reduce_to_fraction(ratio_d)}")
    print(f"Simplifying {ratio_e}: {reduce_to_fraction(ratio_e)}")
    try:
        reduce_to_fraction(ratio_f)
    except ZeroDivisionError as e:
        print(f"Error handling {ratio_f}: {e}")
    print("\nCalculating Ratio Difference:")
    diff1 = calculate_ratio_difference(ratio_a, ratio_b)
    print(f"Difference between {ratio_a} and {ratio_b}: {diff1}")
    diff2 = calculate_ratio_difference(ratio_c, ratio_a)
    print(f"Difference between {ratio_c} and {ratio_a}: {diff2}")
    diff3 = calculate_ratio_difference(ratio_e, ratio_a)
    print(f"Difference between {ratio_e} and {ratio_a}: {diff3}")