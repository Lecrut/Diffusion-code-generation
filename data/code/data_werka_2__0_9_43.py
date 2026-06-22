class LengthConverter:
    def __init__(self):
        self._conversion_factor = 3.28084

    def convert_meters_to_feet(self, meters):
        if not isinstance(meters, (int, float)):
            raise ValueError("Input must be a numeric value.")
        return meters * self._conversion_factor

    def display_conversion(self, meters):
        feet = self.convert_meters_to_feet(meters)
        print(f"{meters} meters is equal to {feet:.2f} feet.")

if __name__ == '__main__':
    sample_value = 10
    converter = LengthConverter()
    result = converter.convert_meters_to_feet(sample_value)
    print(result)
    converter.display_conversion(sample_value)