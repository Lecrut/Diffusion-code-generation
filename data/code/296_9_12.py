def add_ratios(ratio1, ratio2):
    num1, denom1 = map(int, ratio1.split(':'))
    num2, denom2 = map(int, ratio2.split(':'))
    common_denom = denom1 * denom2
    new_num = (num1 * denom2) + (num2 * denom1)
    gcd = gcd_func(new_num, common_denom)
    return f"{new_num // gcd}:{common_denom // gcd}"

def gcd_func(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    print(add_ratios('1:2', '3:4'))