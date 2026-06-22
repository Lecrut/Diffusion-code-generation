import math

def calculate_ratio(numerator, denominator):
    gcd = math.gcd(numerator, denominator)
    return f"{numerator // gcd}:{denominator // gcd}"

if __name__ == '__main__':
    ratio1_numerator = 6
    ratio1_denominator = 9
    result1 = calculate_ratio(ratio1_numerator, ratio1_denominator)
    print(f"Ratio: {ratio1_numerator}/{ratio1_denominator}, Result: {result1}")

    ratio2_numerator = 10
    ratio2_denominator = 15
    result2 = calculate_ratio(ratio2_numerator, ratio2_denominator)
    print(f"Ratio: {ratio2_numerator}/{ratio2_denominator}, Result: {result2}")