class LengthConverter:
    METERS_TO_FEET = 3.28084

    def convert(self, meters):
        if not isinstance(meters, (int, float)):
            raise ValueError("Input must be a numeric value.")
        return meters * self.METERS_TO_FEET

if __name__ == '__main__':
    sample_value = 10
    converter = LengthConverter()
    result = converter.convert(sample_value)
    print(result)