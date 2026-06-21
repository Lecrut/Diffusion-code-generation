class LengthConversion:
    def __init__(self):
        self._METERS_TO_FEET = 3.28084

    def meters_to_feet(self, meters):
        if not isinstance(meters, (int, float)):
            raise ValueError("Input must be a numeric value.")
        return meters * self._METERS_TO_FEET

    def display_conversion(self, meters):
        feet = self.meters_to_feet(meters)
        print(f"{meters} meters is equal to {feet} feet.")

if __name__ == '__main__':
    sample_value = 10
    converter = LengthConversion()
    result = converter.meters_to_feet(sample_value)
    print(result)
    converter.display_conversion(sample_value)