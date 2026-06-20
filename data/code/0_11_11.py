class LengthConverter:
    def __init__(self):
        self._meters_to_feet = 3.28084

    def _validate_input(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        if value < 0:
            raise ValueError("Length cannot be negative")

    def meters_to_feet(self, meters: float) -> float:
        self._validate_input(meters)
        return meters * self._meters_to_feet

if __name__ == '__main__':
    converter = LengthConverter()
    sample_meters = 10
    result_feet = converter.meters_to_feet(sample_meters)
    print(result_feet)