def compute_weight_difference(weights):
    weight1 = weights.get('weight1')
    weight2 = weights.get('weight2')
    if not (isinstance(weight1, (int, float)) and isinstance(weight2, (int, float))):
        raise ValueError("Both weights must be numbers")
    return abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weights = {'weight1': 70.0, 'weight2': 65.0}
    difference = compute_weight_difference(sample_weights)
    print(difference)