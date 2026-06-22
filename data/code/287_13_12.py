class WeightConverter:
    def __init__(self, weights):
        self.weights = weights

    def convert_to_kg(self, weight, unit):
        conversion_factors = {'kg': 1, 'lbs': 0.453592}
        return weight * conversion_factors[unit]

    def calculate_average_weight(self):
        total_weight = sum(self.convert_to_kg(weight, unit) for weight, unit in self.weights)
        average_weight = total_weight / len(self.weights)
        return round(average_weight, 2)

if __name__ == '__main__':
    converter = WeightConverter([(70, 'kg'), (154, 'lbs'), (60, 'kg')])
    print(converter.calculate_average_weight())