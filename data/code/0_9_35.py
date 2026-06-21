class LengthConverter:
    def __init__(self):
        self.METERS_TO_FEET = 3.28084

    def convert(self, meters):
        if not isinstance(meters, (int, float)):
            raise ValueError("Input must be a numeric value.")
        return meters * self.METERS_TO_FEET

    def display_conversion(self, meters):
        feet = self.convert(meters)
        print(f"{meters} meters is equal to {feet} feet.")

if __name__ == '__main__':
    sample_value = 10
    converter = LengthConverter()
    result = converter.convert(sample_value)
    print(result)
    converter.display_conversion(sample_value)