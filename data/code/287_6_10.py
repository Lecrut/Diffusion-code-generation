class WeightCategorizer:
    WEIGHT_RANGES = {
        '0-1kg': [],
        '1-2kg': [],
        '2-3kg': [],
        '3-4kg': []
    }

    @staticmethod
    def categorize_weights(weights):
        for weight in weights:
            if 0 <= weight < 1:
                WeightCategorizer.WEIGHT_RANGES['0-1kg'].append(weight)
            elif 1 <= weight < 2:
                WeightCategorizer.WEIGHT_RANGES['1-2kg'].append(weight)
            elif 2 <= weight < 3:
                WeightCategorizer.WEIGHT_RANGES['2-3kg'].append(weight)
            elif 3 <= weight < 4:
                WeightCategorizer.WEIGHT_RANGES['3-4kg'].append(weight)

        return WeightCategorizer.WEIGHT_RANGES

if __name__ == '__main__':
    weights = [0.5, 1.2, 2.8, 3.9, 0.7]
    categorized_weights = WeightCategorizer.categorize_weights(weights)
    print("Categorized Weights:")
    for range_key, names in categorized_weights.items():
        print(f"{range_key}: {names}")