class DistanceConverter:
    def __init__(self):
        self.units_to_meters = {
            'm': 1.0,
            'km': 1000.0,
            'cm': 0.01,
            'mm': 0.001,
            'mi': 1609.344,
            'yd': 0.9144,
            'ft': 0.3048,
            'in': 0.0254
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.units_to_meters:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if to_unit not in self.units_to_meters:
            raise ValueError(f"Unsupported target unit: {to_unit}")
        
        value_in_meters = value * self.units_to_meters[from_unit]
        converted_value = value_in_meters / self.units_to_meters[to_unit]
        return converted_value

if __name__ == '__main__':
    converter = DistanceConverter()
    result = converter.convert(5, 'km', 'mi')
    print(result)