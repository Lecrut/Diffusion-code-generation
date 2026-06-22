def simplify_ratio(numerator: int, denominator: int) -> tuple:
    gcd = numerator
    while denominator % gcd != 0:
        gcd -= 1
    return (numerator // gcd, denominator // gcd)

def add_ratios(ratio1: tuple, ratio2: tuple) -> tuple:
    new_numerator = ratio1[0] * ratio2[1] + ratio2[0] * ratio1[1]
    new_denominator = ratio1[1] * ratio2[1]
    return simplify_ratio(new_numerator, new_denominator)

if __name__ == '__main__':
    ratio1 = (1, 2)
    ratio2 = (3, 4)
    result = add_ratios(ratio1, ratio2)
    print(result)