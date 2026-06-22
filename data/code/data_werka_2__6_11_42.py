def calculate_weight_difference(weight_data):
    weight1 = weight_data['weight1']
    weight2 = weight_data['weight2']
    return abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weights = {'weight1': 82.0, 'weight2': 76.5}
    difference = calculate_weight_difference(sample_weights)
    print(difference)