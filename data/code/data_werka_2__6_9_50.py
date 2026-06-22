def calculate_absolute_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    weights = {
        'weight_a': 75.5,
        'weight_b': 68.3,
    }
    difference = calculate_absolute_difference(weights['weight_a'], weights['weight_b'])
    print(difference)