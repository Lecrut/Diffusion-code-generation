import math

def convert_weight_ratios(weight1, weight2):
    gcd = math.gcd(int(weight1), int(weight2))
    return (int(weight1) // gcd, int(weight2) // gcd)

if __name__ == '__main__':
    ratio = convert_weight_ratios(45.0, 60.0)
    print(ratio)