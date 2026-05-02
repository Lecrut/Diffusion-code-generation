import math
def calculate_length_ratio(length1: float, length2: float) -> float:
    if length2 == 0.0:
        return float('inf') if length1 != 0.0 else float('nan')
    return length1 / length2
if __name__ == '__main__':
    l1 = 10.0
    l2 = 3.0
    ratio = calculate_length_ratio(l1, l2)
    print(ratio)
    l1_zero = 0.0
    l2_nonzero = 5.0
    ratio_zero = calculate_length_ratio(l1_zero, l2_nonzero)
    print(ratio_zero)
    l1_zero_zero = 0.0
    l2_zero = 0.0
    ratio_nan = calculate_length_ratio(l1_zero_zero, l2_zero)
    print(ratio_nan)
    l1_neg = -10.0
    l2_pos = 2.0
    ratio_neg = calculate_length_ratio(l1_neg, l2_pos)
    print(ratio_neg)