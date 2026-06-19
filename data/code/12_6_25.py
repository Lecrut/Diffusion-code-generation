def convert_weight_ratios(ratios):
    from functools import reduce
    import math

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return abs(a * b) // gcd(a, b)

    total_lcm = reduce(lcm, ratios)
    converted_ratios = [total_lcm // r for r in ratios]
    return converted_ratios

if __name__ == '__main__':
    sample_ratios = [1234567890, 987654321, 111222333]
    result = convert_weight_ratios(sample_ratios)
    print(result)