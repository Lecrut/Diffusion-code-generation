import math

def simplify_weight_ratio(a, b):
    if a == 0 and b == 0:
        return (0, 0)
    gcd = math.gcd(a, b)
    return (a // gcd, b // gcd)

if __name__ == '__main__':
    ratio1 = simplify_weight_ratio(98, 42)
    print(ratio1)
    ratio2 = simplify_weight_ratio(0, 5)
    print(ratio2)
    ratio3 = simplify_weight_ratio(7, 0)
    print(ratio3)
    ratio4 = simplify_weight_ratio(0, 0)
    print(ratio4)