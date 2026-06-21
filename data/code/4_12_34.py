class DistanceConverter:
    def __init__(self):
        self.conversion_factors = {
            'm_to_km': 1 / 1000,
            'km_to_m': 1000
        }

    def convert(self, value, unit):
        if unit not in self.conversion_factors:
            raise ValueError("Unsupported unit. Use 'm_to_km' for meters to kilometers or 'km_to_m' for kilometers to meters.")
        return value * self.conversion_factors[unit]

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_values = [
        (1500, 'm_to_km'),
        (2.5, 'km_to_m')
    ]
    for value, unit in sample_values:
        converted_value = converter.convert(value, unit)
        print(f"{value} {unit.split('_')[0]} is {converted_value} {unit.split('_')[1]}")