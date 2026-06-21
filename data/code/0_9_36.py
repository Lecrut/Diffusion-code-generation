class LengthConversion:
    CONVERSION_FACTOR = 3.28084

    @staticmethod
    def validate_input(value):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be a numeric value.")
        if value < 0:
            raise ValueError("Length cannot be negative.")

    def meters_to_feet(self, meters):
        self.validate_input(meters)
        return meters * self.CONVERSION_FACTOR

if __name__ == '__main__':
    sample_value = 10
    converter = LengthConversion()
    result = converter.meters_to_feet(sample_value)
    print(result)