def compute_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    weights = {'weight1': 80.5, 'weight2': 76.3}
    difference = compute_weight_difference(weights['weight1'], weights['weight2'])
    print(difference)