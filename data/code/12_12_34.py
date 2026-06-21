import math

def convert_weight_ratios(weight1, weight2):
    try:
        weight1_int = int(weight1)
        weight2_int = int(weight2)
        gcd = math.gcd(weight1_int, weight2_int)
        return (weight1_int // gcd, weight2_int // gcd)
    except ValueError:
        raise ValueError("Both inputs must be numeric types that can be converted to integers.")

if __name__ == '__main__':
    sample_weight1 = 90.0
    sample_weight2 = 120.0
    result = convert_weight_ratios(sample_weight1, sample_weight2)
    print(result)