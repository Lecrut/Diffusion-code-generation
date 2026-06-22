def simplify_ratio(ratio1, ratio2):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    common_divisor = gcd(ratio1, ratio2)
    simplified_ratio = (ratio1 // common_divisor, ratio2 // common_divisor)
    return simplified_ratio

if __name__ == '__main__':
    ratio1 = 48
    ratio2 = 180
    print(simplify_ratio(ratio1, ratio2))