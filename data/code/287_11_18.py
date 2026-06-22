class WeightConverter:
    def __init__(self):
        self.conversion_factors = {'kg': 1, 'lbs': 0.453592}

    def convert_weight(self, value, unit):
        return value * self.conversion_factors[unit]

    def print_table(self, weights):
        headers = ["Original Value", "Unit", "Converted (kg)"]
        print("\t".join(headers))
        for weight in weights:
            print("\t".join(map(str, weight)))

if __name__ == '__main__':
    converter = WeightConverter()
    sample_weights = [('70', 'kg'), ('154', 'lbs'), ('60', 'kg')]
    converted_weights = [(float(value), unit, converter.convert_weight(float(value), unit)) for value, unit in sample_weights]
    converter.print_table(converted_weights)