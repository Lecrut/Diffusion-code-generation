import math

def calculate_ratio(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    
    common_divisor = math.gcd(numerator, denominator)
    simplified_num = numerator // common_divisor
    simplified_den = denominator // common_divisor
    
    return f"{simplified_num}:{simplified_den}"

if __name__ == '__main__':
    ratio1 = (6, 9)
    result1 = calculate_ratio(*ratio1)
    print(f"Ratio: {ratio1}, Result: {result1}")
    
    ratio2 = (10, 15)
    result2 = calculate_ratio(*ratio2)
    print(f"Ratio: {ratio2}, Result: {result2}")