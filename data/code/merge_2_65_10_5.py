class LengthConverter:
    def convert(self, value, from_unit, to_unit):
        if value < 0:
            raise ValueError("Length must be non-negative.")
        conversion_factors = {
            'meters': 1,
            'kilometers': 1e-3,
            'centimeters': 1e2,
            'millimeters': 1e3,
        }
        if from_unit not in conversion_factors or to_unit not in conversion_factors:
            raise ValueError("Invalid unit. Supported units: meters, kilometers, centimeters, millimeters.")
        value_in_meters = value * conversion_factors[from_unit]
        converted_value = value_in_meters / conversion_factors[to_unit]
        return round(converted_value, 6)
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(1000, 'meters', 'kilometers'))                   
    print(converter.convert(50, 'centimeters', 'millimeters'))                  
    try:
        converter.convert(-10, 'meters', 'meters')
    except ValueError as e:
        print(f"Error: {e}")