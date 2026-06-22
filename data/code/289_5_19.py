class DistanceConverter:
    def __init__(self):
        self.conversions = {
            'yd': 0.9144,
            'm': 1.0
        }

    def convert(self, value, from_unit, to_unit):
        if value < 0:
            raise ValueError("Value must be non-negative")
        if from_unit not in self.conversions or to_unit not in self.conversions:
            raise ValueError("Invalid unit specified")
        base_value = value * self.conversions[from_unit] / self.conversions[to_unit]
        return base_value

if __name__ == '__main__':
    converter = DistanceConverter()
    print(f"10 yd to m: {converter.convert(10, 'yd', 'm'):.2f}")
    print(f"5 m to yd: {converter.convert(5, 'm', 'yd'):.2f}")