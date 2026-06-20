class DistanceConverter:
    def __init__(self):
        self.conversion_factors = {
            'm': {'m': 1.0, 'km': 0.001, 'mi': 0.000621371},
            'km': {'m': 1000.0, 'km': 1.0, 'mi': 0.621371},
            'mi': {'m': 1609.34, 'km': 1.60934, 'mi': 1.0}
        }

    def convert(self, value, from_unit, to_unit):
        if value < 0:
            raise ValueError("Distance cannot be negative")
        if from_unit not in self.conversion_factors:
            raise ValueError(f"Invalid from_unit: {from_unit}. Must be 'm', 'km', or 'mi'.")
        if to_unit not in self.conversion_factors[from_unit]:
            raise ValueError(f"Invalid to_unit: {to_unit}. Must be 'm', 'km', or 'mi'.")
        factor = self.conversion_factors[from_unit][to_unit]
        return value * factor

def adjust_distance(value, from_unit, to_unit):
    converter = DistanceConverter()
    return converter.convert(value, from_unit, to_unit)

if __name__ == '__main__':
    sample_values = [
        (1000, 'm', 'km'),
        (1, 'km', 'm'),
        (1, 'mi', 'km'),
        (5, 'km', 'mi'),
        (0, 'm', 'm'),
        (100, 'm', 'mi'),
    ]

    for val, from_u, to_u in sample_values:
        result = adjust_distance(val, from_u, to_u)
        print(f"{val} {from_u} = {result} {to_u}")

    try:
        adjust_distance(-5, 'm', 'km')
    except ValueError as e:
        print(e)

    try:
        adjust_distance(5, 'ft', 'm')
    except ValueError as e:
        print(e)