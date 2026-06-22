def calculate_weight_difference(weight1: float, weight2: float) -> float:
    def absolute_difference(a: float, b: float) -> float:
        return abs(a - b)
    
    return absolute_difference(weight1, weight2)

if __name__ == '__main__':
    sample_weights = {
        'weight1': 80.7,
        'weight2': 72.4
    }
    difference = calculate_weight_difference(sample_weights['weight1'], sample_weights['weight2'])
    print(difference)