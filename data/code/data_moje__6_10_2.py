import sys

def calculate_weight_difference(weights):
    if not weights:
        return 0
    return max(weights) - min(weights)

if __name__ == '__main__':
    sample_weights = [10, 25, 3, 40, 15]
    result = calculate_weight_difference(sample_weights)
    print(result)