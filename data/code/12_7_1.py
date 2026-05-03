import math
def ratio_conversion(ratio_a, ratio_b):
    if ratio_b == 0:
        return float('inf') if ratio_a != 0 else float('nan')
    numerator = ratio_a * ratio_b
    denominator = ratio_b * ratio_b
    return numerator / denominator
if __name__ == '__main__':
    ratio1 = 123456789012345
    ratio2 = 987654321098765
    result = ratio_conversion(ratio1, ratio2)
    print(result)