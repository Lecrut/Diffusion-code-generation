class LengthConverter:
    def to_meters(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Input must be a non-negative number")
        return value * self._get_multiplier('m')
    def to_kilometers(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Input must be a non-negative number")
        return value / 1000.0
    def to_centimeters(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Input must be a non-negative number")
        return value * 100.0
    def to_millimeters(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Input must be a non-negative number")
        return value * 1000.0
    @staticmethod
    def _get_multiplier(unit):
        multipliers = {
            'm': 1,
            'km': 1e-3,
            'cm': 100,
            'mm': 1000
        }
        return multipliers.get(unit)
if __name__ == '__main__':
    converter = LengthConverter()
    sample_inputs = [5.2, -3, 0]
    for input_val in sample_inputs:
        try:
            print(f"Converting {input_val} meters:")
            print(f"  Kilometers: {converter.to_kilometers(input_val)}")
            print(f"  Centimeters: {converter.to_centimeters(input_val)}")
            print(f"  Millimeters: {converter.to_millimeters(input_val)}")
        except ValueError as e:
            print(f"Error converting {input_val}: {e}")