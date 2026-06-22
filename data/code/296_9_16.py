def simplify_ratio(numerator, denominator):
    gcd = max(numerator, denominator)
    while gcd > 1:
        if numerator % gcd == 0 and denominator % gcd == 0:
            break
        gcd -= 1
    return (numerator // gcd, denominator // gcd)

def add_ratios(ratio1, ratio2):
    num1, den1 = ratio1
    num2, den2 = ratio2
    common_den = den1 * den2
    new_num = num1 * den2 + num2 * den1
    return simplify_ratio(new_num, common_den)

if __name__ == '__main__':
    ratio1 = (3, 4)
    ratio2 = (5, 6)
    result = add_ratios(ratio1, ratio2)
    print(result)