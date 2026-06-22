def categorize_weights(weights):
    weight_ranges = {
        '0-1kg': [],
        '1-2kg': [],
        '2-3kg': [],
        '3-4kg': [],
        '4-5kg': []
    }
    for weight in weights:
        if 0 <= weight < 1:
            weight_ranges['0-1kg'].append(weight)
        elif 1 <= weight < 2:
            weight_ranges['1-2kg'].append(weight)
        elif 2 <= weight < 3:
            weight_ranges['2-3kg'].append(weight)
        elif 3 <= weight < 4:
            weight_ranges['3-4kg'].append(weight)
        elif 4 <= weight < 5:
            weight_ranges['4-5kg'].append(weight)
    return weight_ranges

if __name__ == '__main__':
    sample_weights = [0.5, 1.2, 2.8, 3.9, 4.5, 5.1]
    categorized_weights = categorize_weights(sample_weights)
    print(categorized_weights)