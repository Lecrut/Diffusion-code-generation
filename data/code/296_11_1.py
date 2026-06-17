import math
def scale_ratio(ratio, factor):
    num = ratio[0] * factor
    den = ratio[1] * factor
    common_divisor = math.gcd(num, den)
    new_num = num // common_divisor
    new_den = den // common_divisor
    return (new_num, new_den)
if __name__ == '__main__':
    ratio1 = (4, 6)
    factor1 = 3
    result1 = scale_ratio(ratio1, factor1)
    print(f"Ratio: {ratio1}, Factor: {factor1}, Scaled Ratio: {result1}")
    ratio2 = (10, 15)
    factor2 = 4
    result2 = scale_ratio(ratio2, factor2)
    print(f"Ratio: {ratio2}, Factor: {factor2}, Scaled Ratio: {result2}")
    ratio3 = (7, 11)
    factor3 = 5
    result3 = scale_ratio(ratio3, factor3)
    print(f"Ratio: {ratio3}, Factor: {factor3}, Scaled Ratio: {result3}")