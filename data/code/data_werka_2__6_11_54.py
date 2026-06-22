def compute_weight_difference(weights):
    return abs(weights['weight1'] - weights['weight2'])

if __name__ == '__main__':
    sample_weights = {'weight1': 70.0, 'weight2': 63.8}
    difference = compute_weight_difference(sample_weights)
    print(difference)