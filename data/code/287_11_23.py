class WeightConverter:
    def __init__(self):
        self.conversion_factors = {'kg': 1, 'lbs': 0.453592}

    def convert_weight(self, value, unit):
        if unit == 'kg':
            return value
        elif unit == 'lbs':
            return value * self.conversion_factors['lbs']
        else:
            raise ValueError(f"Unknown unit: {unit}")

    def print_table(self, weights):
        headers = ["Original Value", "Unit", "Converted (kg)"]
        print("\t".join(headers))
        for weight in weights:
            print("\t".join(map(str, weight)))

if __name__ == '__main__':
    converter = WeightConverter()
    raw_data = [
        ('70', 'kg'),
        ('154', 'lbs'),
        ('60', 'kg')
    ]
    converted_weights = [(float(value), unit, converter.convert_weight(float(value), unit)) for value, unit in raw_data]
    converter.print_table(converted_weights)