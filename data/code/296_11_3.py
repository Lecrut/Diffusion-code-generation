import math
def scale_ratio(ratio, factor):
    num, den = ratio
    new_num = num * factor
    new_den = den * factor
    common_divisor = math.gcd(new_num, new_den)
    simplified_num = new_num // common_divisor
    simplified_den = new_den // common_divisor
    return (simplified_num, simplified_den)
if __name__ == '__main__':
    ratio1 = (6, 8)
    factor1 = 3
    result1 = scale_ratio(ratio1, factor1)
    print(f"Ratio: {ratio1}, Factor: {factor1}, Scaled Ratio: {result1}")
    ratio2 = (10, 15)
    factor2 = 4
    result2 = scale_ratio(ratio2, factor2)
    print(f"Ratio: {ratio2}, Factor: {factor2}, Scaled Ratio: {result2}")
    ratio3 = (7, 11)
    factor3 = 2
    result3 = scale_ratio(ratio3, factor3)
    print(f"Ratio: {ratio3}, Factor: {factor3}, Scaled Ratio: {result3}")
    ratio4 = (12, 18)
    factor4 = 5
    result4 = scale_ratio(ratio4, factor4)
    print(f"Ratio: {ratio4}, Factor: {factor4}, Scaled Ratio: {result4}")