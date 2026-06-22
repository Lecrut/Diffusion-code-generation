class DistanceConverter:
    def __init__(self):
        self.factors_to_meters = {
            'm': 1.0,
            'km': 1000.0,
            'cm': 0.01,
            'mm': 0.001,
            'ft': 0.3048,
            'in': 0.0254,
            'yd': 0.9144,
            'mi': 1609.344
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.factors_to_meters:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if to_unit not in self.factors_to_meters:
            raise ValueError(f"Unsupported target unit: {to_unit}")
        
        meters = value * self.factors_to_meters[from_unit]
        return meters / self.factors_to_meters[to_unit]

if __name__ == '__main__':
    converter = DistanceConverter()
    result = converter.convert(100, 'cm', 'm')
    print(result)
    result = converter.convert(1, 'mi', 'km')
    print(result)
    result = converter.convert(12, 'in', 'cm')
    print(result)
    try:
        result = converter.convert(10, 'xyz', 'm')
        print(result)
    except ValueError as e:
        print(e)