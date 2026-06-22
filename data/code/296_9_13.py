def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def simplify_ratio(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)

def add_ratios(ratio1, ratio2):
    numerator1, denominator1 = ratio1
    numerator2, denominator2 = ratio2
    lcm_denominator = denominator1 * denominator2 // gcd(denominator1, denominator2)
    new_numerator = numerator1 * (lcm_denominator // denominator1) + numerator2 * (lcm_denominator // denominator2)
    return simplify_ratio(new_numerator, lcm_denominator)
if __name__ == '__main__':
    ratio1 = (3, 4)
    ratio2 = (1, 8)
    result = add_ratios(ratio1, ratio2)
    print(result)