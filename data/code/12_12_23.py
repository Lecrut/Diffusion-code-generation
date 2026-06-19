import math

def convert_weight_ratios(weight1, weight2):
    gcd = math.gcd(weight1, weight2)
    return (weight1 // gcd, weight2 // gcd)

if __name__ == '__main__':
    sample_weight1 = 80
    sample_weight2 = 120
    result = convert_weight_ratios(sample_weight1, sample_weight2)
    print(result)