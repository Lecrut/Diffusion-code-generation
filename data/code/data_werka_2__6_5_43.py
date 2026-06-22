Kilograms = 1

def compute_weight_difference(weight1, weight2):
    if not (isinstance(weight1, (int, float)) and isinstance(weight2, (int, float))):
        raise ValueError('Both inputs must be numbers.')
    return abs(weight1 - weight2) * Kilograms
if __name__ == '__main__':
    sample_weight1 = 85
    sample_weight2 = 70
    print(compute_weight_difference(sample_weight1, sample_weight2))