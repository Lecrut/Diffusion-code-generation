class UnitConverter:
    def __init__(self):
        self.conversion_factors = {
            'meters': {'centimeters': 100, 'millimeters': 1000, 'kilometers': 0.001},
            'centimeters': {'meters': 0.01, 'millimeters': 10, 'kilometers': 0.00001},
            'millimeters': {'meters': 0.001, 'centimeters': 0.1, 'kilometers': 0.000001},
            'kilometers': {'meters': 1000, 'centimeters': 100000, 'millimeters': 1000000}
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported base unit: {from_unit}")
        if to_unit not in self.conversion_factors[from_unit]:
            raise ValueError(f"Conversion to {to_unit} from {from_unit} is not supported")
        
        conversion_factor = self.conversion_factors[from_unit][to_unit]
        return value * conversion_factor

if __name__ == '__main__':
    converter = UnitConverter()
    sample_value = 5.0
    from_unit = 'meters'
    to_unit = 'centimeters'
    result = converter.convert(sample_value, from_unit, to_unit)
    print(f"{sample_value} {from_unit} is equal to {result} {to_unit}")