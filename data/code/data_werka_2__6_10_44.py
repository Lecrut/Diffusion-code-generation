def validate_weights(weight1, weight2):
    if not (isinstance(weight1, (int, float)) and isinstance(weight2, (int, float))):
        raise ValueError("Both weights must be numbers.")

def compute_weight_difference(weight1, weight2):
    validate_weights(weight1, weight2)
    return abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weight1 = 80.5
    sample_weight2 = 73.9
    difference = compute_weight_difference(sample_weight1, sample_weight2)
    print(difference)