import math
def simplify_fraction(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    common = math.gcd(numerator, denominator)
    return numerator // common, denominator // common
if __name__ == '__main__':
    length1 = 12
    length2 = 18
    numerator = length1
    denominator = length2
    num, den = simplify_fraction(numerator, denominator)
    print(f"The ratio of {length1} to {length2} is {num}/{den}")