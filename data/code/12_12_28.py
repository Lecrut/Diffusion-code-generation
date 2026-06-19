import math

def convert_weight_ratios(weight1, weight2):
    gcd_value = math.gcd(int(weight1), int(weight2))
    return (int(weight1) // gcd_value, int(weight2) // gcd_value)

if __name__ == '__main__':
    sample_weight1 = 80
    sample_weight2 = 120
    result = convert_weight_ratios(sample_weight1, sample_weight2)
    print(result)