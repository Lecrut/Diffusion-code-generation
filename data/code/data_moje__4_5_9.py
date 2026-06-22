class UnitConverter:
    def __init__(self):
        self.to_meters = {
            'm': 1.0,
            'km': 1000.0,
            'cm': 0.01,
            'mm': 0.001,
            'mi': 1609.34,
            'ft': 0.3048,
            'in': 0.0254,
            'yd': 0.9144
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.to_meters:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if to_unit not in self.to_meters:
            raise ValueError(f"Unsupported target unit: {to_unit}")
        if value < 0:
            raise ValueError("Distance cannot be negative")
        meters = value * self.to_meters[from_unit]
        result = meters / self.to_meters[to_unit]
        return result

if __name__ == '__main__':
    converter = UnitConverter()
    test_distance = 5
    source = 'km'
    target = 'mi'
    converted_value = converter.convert(test_distance, source, target)
    print(f"{test_distance} {source} is {converted_value} {target}")