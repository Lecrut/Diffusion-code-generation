from math import gcd

def simplify_ratio(ratio):
    num1, den1 = ratio[0]
    num2, den2 = ratio[1]
    total_num = num1 * den2 + num2 * den1
    total_den = den1 * den2
    common_divisor = gcd(total_num, total_den)
    return (total_num // common_divisor, total_den // common_divisor)

if __name__ == '__main__':
    ratio1 = (3, 4)
    ratio2 = (5, 6)
    result = simplify_ratio((ratio1, ratio2))
    print(result)