import math
def simplify_ratio(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    common = math.gcd(a, b)
    return a // common, b // common
if __name__ == '__main__':
    ratio1_num = 12
    ratio1_den = 18
    ratio2_num = 20
    ratio2_den = 30
    try:
        num1, den1 = int(ratio1_num), int(ratio1_den)
        num2, den2 = int(ratio2_num), int(ratio2_den)
        if den1 == 0 or den2 == 0:
            raise ValueError("One of the denominators is zero")
        simplified1 = simplify_ratio(num1, den1)
        simplified2 = simplify_ratio(num2, den2)
        print(f"Original Ratio 1: {num1}/{den1}")
        print(f"Simplified Ratio 1: {simplified1[0]}/{simplified1[1]}")
        print(f"Original Ratio 2: {num2}/{den2}")
        print(f"Simplified Ratio 2: {simplified2[0]}/{simplified2[1]}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")