import math

def convert_weight_ratios(weight1, weight2):
    int_weight1 = int(weight1)
    int_weight2 = int(weight2)
    gcd_value = math.gcd(int_weight1, int_weight2)
    simplified_ratio = (int_weight1 // gcd_value, int_weight2 // gcd_value)
    return simplified_ratio
if __name__ == '__main__':
    sample_weight1 = 90.0
    sample_weight2 = 120.0
    result = convert_weight_ratios(sample_weight1, sample_weight2)
    print(result)