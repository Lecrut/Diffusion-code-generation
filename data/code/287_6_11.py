def categorize_weights(weights):
    weight_bins = {
        '0-1kg': [],
        '1-2kg': [],
        '2-3kg': [],
        '3-4kg': [],
        '4-5kg': []
    }
    
    for weight in weights:
        if 0 < weight <= 1:
            weight_bins['0-1kg'].append(weight)
        elif 1 < weight <= 2:
            weight_bins['1-2kg'].append(weight)
        elif 2 < weight <= 3:
            weight_bins['2-3kg'].append(weight)
        elif 3 < weight <= 4:
            weight_bins['3-4kg'].append(weight)
        elif 4 < weight <= 5:
            weight_bins['4-5kg'].append(weight)
    
    return weight_bins

if __name__ == '__main__':
    sample_weights = [0.5, 1.2, 2.8, 3.6, 4.4, 5.1, 0.9]
    categorized_weights = categorize_weights(sample_weights)
    print("Categorized Weights:")
    for bin_name, weights in categorized_weights.items():
        print(f"{bin_name}: {weights}")