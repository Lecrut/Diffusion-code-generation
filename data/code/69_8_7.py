class UnitConverter:
    def __init__(self):
        self.conversion_factors = {
            'miles_to_feet': 5280,
            'feet_to_miles': 1 / 5280,
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        
        factor_key = f"{from_unit}_to_{to_unit}"
        
        if factor_key not in self.conversion_factors:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
        return value * self.conversion_factors[factor_key]

if __name__ == '__main__':
    converter = UnitConverter()
    result = converter.convert(5, 'miles', 'feet')
    print(result)