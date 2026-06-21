class WeightConverter:
    def __init__(self):
        self.conversion_factors = {
            'kg_to_pounds': 2.20462,
            'pounds_to_kg': 1 / 2.20462
        }

    def convert(self, value, from_unit, to_unit):
        if f"{from_unit}_to_{to_unit}" in self.conversion_factors:
            return value * self.conversion_factors[f"{from_unit}_to_{to_unit}"]
        else:
            raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")

if __name__ == '__main__':
    converter = WeightConverter()
    sample_kg = 90
    sample_pounds = 198
    converted_pounds = converter.convert(sample_kg, 'kg', 'pounds')
    converted_kg = converter.convert(sample_pounds, 'pounds', 'kg')
    print(f"{sample_kg} kg is {converted_pounds:.2f} pounds")
    print(f"{sample_pounds} pounds is {converted_kg:.2f} kg")