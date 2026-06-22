def calculate_absolute_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    weights = {
        'weight1': 70.0,
        'weight2': 65.4
    }
    difference = calculate_absolute_difference(weights['weight1'], weights['weight2'])
    print(difference)