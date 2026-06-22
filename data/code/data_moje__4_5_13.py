class DistanceConverter:
    def __init__(self):
        self.units = {
            "m": 1.0,
            "km": 1000.0,
            "cm": 0.01,
            "mm": 0.001,
            "mi": 1609.344,
            "yd": 0.9144,
            "ft": 0.3048,
            "in": 0.0254,
            "nm": 1e-9,
            "um": 1e-6
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.units:
            raise ValueError(f"Unknown source unit: {from_unit}")
        if to_unit not in self.units:
            raise ValueError(f"Unknown target unit: {to_unit}")
        
        base_value = value * self.units[from_unit]
        result = base_value / self.units[to_unit]
        return result

def convert_distance(distance_value, from_unit, to_unit):
    converter = DistanceConverter()
    return converter.convert(distance_value, from_unit, to_unit)

if __name__ == '__main__':
    result = convert_distance(100, "km", "mi")
    print(result)