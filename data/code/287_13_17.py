class WeightCalculator:
    def __init__(self):
        self.conversion_factors = {'kg': 1, 'lbs': 0.453592}

    def convert_to_kg(self, weight, unit):
        return weight * self.conversion_factors[unit]

    def calculate_average_weight(self, weights):
        total_weight = sum(self.convert_to_kg(weight, unit) for weight, unit in weights)
        average_weight = total_weight / len(weights)
        return round(average_weight, 2)

if __name__ == '__main__':
    calculator = WeightCalculator()
    sample_weights = [(70, 'kg'), (154, 'lbs'), (60, 'kg')]
    print(calculator.calculate_average_weight(sample_weights))