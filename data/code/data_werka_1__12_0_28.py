from math import gcd

def simplify_ratio(ratio1, ratio2):
    numbers = [num for pair in (ratio1, ratio2) for num in pair]
    common_divisor = gcd(*numbers)
    simplified_numbers = [num // common_divisor for num in numbers]
    return tuple(simplified_numbers)
if __name__ == '__main__':
    ratio1 = (4, 8)
    ratio2 = (6, 9)
    result = simplify_ratio(ratio1, ratio2)
    print(result)