class FootToMeterConverter:
    def __init__(self):
        self.conversion_factor = 0.3048

    def convert(self, feet):
        if not isinstance(feet, (int, float)):
            raise ValueError("Invalid input: Expected a number")
        return feet * self.conversion_factor

if __name__ == '__main__':
    converter = FootToMeterConverter()
    sample_feet = 10
    meters = converter.convert(sample_feet)
    print(f"{sample_feet} feet is equal to {meters:.2f} meters")