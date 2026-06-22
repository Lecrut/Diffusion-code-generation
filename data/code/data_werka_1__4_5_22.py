class DistanceConverter:
    def __init__(self):
        self.conversion_factors = {
            'm': 1.0,
            'km': 1000.0,
            'cm': 0.01,
            'mm': 0.001,
            'in': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144,
            'mi': 1609.34
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError("Unsupported unit")
        
        factor_from = self.conversion_factors[from_unit]
        factor_to = self.conversion_factors[to_unit]
        
        converted_value = (value * factor_from) / factor_to
        return converted_value

if __name__ == '__main__':
    converter = DistanceConverter()
    
    try:
        value = 10
        from_unit = 'km'
        to_unit = 'mi'
        result = converter.convert(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result} {to_unit}")
    except ValueError as e:
        print(e)