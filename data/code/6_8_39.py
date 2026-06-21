class WeightCalculator:
    @staticmethod
    def calculate_difference(weights):
        if not weights:
            raise ValueError("The list of weights cannot be empty.")
        max_weight = max(weights)
        min_weight = min(weights)
        return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [10.5, 20.3, 5.8, 40.9, 25.6]
    calculator = WeightCalculator()
    difference = calculator.calculate_difference(sample_weights)
    print(difference)