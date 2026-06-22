import math

def calculate_ratio(numerator, denominator):
    common_divisor = math.gcd(numerator, denominator)
    simplified_numerator = numerator // common_divisor
    simplified_denominator = denominator // common_divisor
    return f"{simplified_numerator}:{simplified_denominator}"

if __name__ == '__main__':
    ratio1 = (9, 12)
    result1 = calculate_ratio(ratio1[0], ratio1[1])
    print(f"Ratio: {ratio1}, Result: {result1}")
    
    ratio2 = (25, 35)
    result2 = calculate_ratio(ratio2[0], ratio2[1])
    print(f"Ratio: {ratio2}, Result: {result2}")