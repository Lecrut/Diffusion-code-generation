def calculate_weight_difference(weights):
    if not weights:
        raise ValueError("The list of weights cannot be empty.")
    
    weight_extremes = {'max': float('-inf'), 'min': float('inf')}
    
    for weight in weights:
        if weight > weight_extremes['max']:
            weight_extremes['max'] = weight
        if weight < weight_extremes['min']:
            weight_extremes['min'] = weight
    
    return weight_extremes['max'] - weight_extremes['min']

if __name__ == '__main__':
    sample_weights = [10.5, 20.3, 5.8, 40.7, 15.2]
    difference = calculate_weight_difference(sample_weights)
    print(difference)