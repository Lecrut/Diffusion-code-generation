class UnitConverter:
    def __init__(self):
        self.conversion_factors = {
            'meters_to_feet': 3.28084,
        }
    
    def convert(self, value, conversion_key):
        if conversion_key not in self.conversion_factors:
            raise ValueError(f"Unsupported conversion key: {conversion_key}")
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be a numeric value.")
        return value * self.conversion_factors[conversion_key]

if __name__ == '__main__':
    sample_value = 10
    converter = UnitConverter()
    result = converter.convert(sample_value, 'meters_to_feet')
    print(result)