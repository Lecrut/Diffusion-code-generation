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
    ratio1 = (6, 9)
    factor1 = 2
    result1 = scale_ratio(ratio1, factor1)
    print(f"Initial ratio: {ratio1}, Factor: {factor1}, Scaled ratio: {result1}")
    ratio2 = (10, 15)
    factor2 = 3
    result2 = scale_ratio(ratio2, factor2)
    print(f"Initial ratio: {ratio2}, Factor: {factor2}, Scaled ratio: {result2}")
    ratio3 = (7, 11)
    factor3 = 4
    result3 = scale_ratio(ratio3, factor3)
    print(f"Initial ratio: {ratio3}, Factor: {factor3}, Scaled ratio: {result3}")
    ratio4 = (12, 18)
    factor4 = 5
    result4 = scale_ratio(ratio4, factor4)
    print(f"Initial ratio: {ratio4}, Factor: {factor4}, Scaled ratio: {result4}")