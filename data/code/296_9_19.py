def add_ratios(ratio1, ratio2):
    numerator = ratio1[0] * ratio2[1] + ratio2[0] * ratio1[1]
    denominator = ratio1[1] * ratio2[1]
    return (numerator, denominator)

def simplify_ratio(numerator, denominator):
    gcd = abs(numerator)
    while gcd > 1:
        if numerator % gcd == 0 and denominator % gcd == 0:
            break
        gcd -= 1
    return (numerator // gcd, denominator // gcd)

def sum_ratios(ratio1, ratio2):
    result_ratio = add_ratios(ratio1, ratio2)
    simplified_result = simplify_ratio(result_ratio[0], result_ratio[1])
    return simplified_result

if __name__ == '__main__':
    ratio1 = (1, 3)
    ratio2 = (1, 6)
    print(sum_ratios(ratio1, ratio2))