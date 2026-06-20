import sys

def compute_weight_difference(weight_a, weight_b):
    return abs(weight_a - weight_b)

if __name__ == '__main__':
    sample_weight_1 = 150.5
    sample_weight_2 = 142.3
    result = compute_weight_difference(sample_weight_1, sample_weight_2)
    print(result)