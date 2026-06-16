import math
def scale_ratio(ratio_a, ratio_b, factor):
    new_a = ratio_a * factor
    new_b = ratio_b * factor
    return new_a, new_b
if __name__ == '__main__':
    original_a = 2
    original_b = 3
    scale_factor = 5.5
    new_a, new_b = scale_ratio(original_a, original_b, scale_factor)
    print(f"Original Ratio: {original_a}:{original_b}")
    print(f"Scaling Factor: {scale_factor}")
    print(f"New Scaled Ratio: {new_a}:{new_b}")