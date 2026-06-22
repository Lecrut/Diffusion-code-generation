def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def simplify_ratio(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    simplified_numerator = numerator // common_divisor
    simplified_denominator = denominator // common_divisor
    return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    num1 = 1000000000000000000000000000000
    num2 = 400000000000000000000000000000
    result = simplify_ratio(num1, num2)
    print(result)