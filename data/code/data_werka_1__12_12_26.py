import math

def convert_weight_ratios(weight1, weight2):
    gcd = math.gcd(int(weight1), int(weight2))
    return (int(weight1) // gcd, int(weight2) // gcd)

if __name__ == '__main__':
    weight1 = 45.0
    weight2 = 60.0
    result = convert_weight_ratios(weight1, weight2)
    print(result)