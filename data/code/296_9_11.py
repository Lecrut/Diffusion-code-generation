def simplify_ratio(numerator, denominator):
    gcd = 1
    for i in range(2, min(numerator, denominator) + 1):
        if numerator % i == 0 and denominator % i == 0:
            gcd = i
    return (numerator // gcd, denominator // gcd)

def add_ratios(ratio1, ratio2):
    num1, den1 = ratio1
    num2, den2 = ratio2
    common_denominator = den1 * den2
    new_numerator = num1 * den2 + num2 * den1
    return simplify_ratio(new_numerator, common_denominator)
if __name__ == '__main__':
    ratio1 = (3, 4)
    ratio2 = (1, 2)
    result = add_ratios(ratio1, ratio2)
    print(result)