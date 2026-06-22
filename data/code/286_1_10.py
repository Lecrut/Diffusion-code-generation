class FootToMeterConverter:

    def __init__(self):
        self.conversion_factor = 0.3048

    def convert(self, feet):
        try:
            feet_value = float(feet)
            meters = feet_value * self.conversion_factor
            return meters
        except ValueError:
            return None
if __name__ == '__main__':
    converter = FootToMeterConverter()
    sample_feet = 10
    result = converter.convert(sample_feet)
    print(result)