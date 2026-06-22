def categorize_weights(weight_list):
    weight_categories = {
        '0-1kg': [],
        '1-2kg': [],
        '2-3kg': []
    }
    for weight in weight_list:
        if 0 < weight <= 1:
            weight_categories['0-1kg'].append('Item A')
        elif 1 < weight <= 2:
            weight_categories['1-2kg'].append('Item B')
        elif 2 < weight <= 3:
            weight_categories['2-3kg'].append('Item C')
    return weight_categories

if __name__ == '__main__':
    sample_weights = [0.5, 1.2, 1.8, 2.5, 3.1]
    categorized_weights = categorize_weights(sample_weights)
    for category, items in categorized_weights.items():
        print(f"{category}: {items}")