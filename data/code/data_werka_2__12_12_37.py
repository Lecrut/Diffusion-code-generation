import math

def convert_weight_ratios(weight1, weight2):
    gcd = math.gcd(int(weight1), int(weight2))
    return (int(weight1) // gcd, int(weight2) // gcd)

if __name__ == '__main__':
    SAMPLE_WEIGHT_1 = 90.0
    SAMPLE_WEIGHT_2 = 120.0
    result = convert_weight_ratios(SAMPLE_WEIGHT_1, SAMPLE_WEIGHT_2)
    print(result)