import math

def convert_weight_ratios(weight1, weight2):
    weight1_int = int(weight1)
    weight2_int = int(weight2)
    common_divisor = math.gcd(weight1_int, weight2_int)
    simplified_ratio = (weight1_int // common_divisor, weight2_int // common_divisor)
    return simplified_ratio

if __name__ == '__main__':
    sample_weight1 = 90
    sample_weight2 = 135
    result = convert_weight_ratios(sample_weight1, sample_weight2)
    print(result)