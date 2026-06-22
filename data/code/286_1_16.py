class FeetToMeterConverter:
    def __init__(self):
        self.conversion_factor = 0.3048

    def convert(self, feet):
        try:
            meters = feet * self.conversion_factor
            return meters
        except (ValueError, TypeError) as e:
            raise ValueError("Invalid input: Please provide a numeric value for feet.") from e

if __name__ == '__main__':
    converter = FeetToMeterConverter()
    sample_feet = 10
    try:
        result = converter.convert(sample_feet)
        print(f"{sample_feet} feet is equal to {result} meters.")
    except ValueError as e:
        print(e)