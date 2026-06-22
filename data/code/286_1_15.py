class FootToMeterConverter:
    def __init__(self):
        self.conversion_factor = 0.3048

    def convert(self, feet):
        try:
            return feet * self.conversion_factor
        except TypeError:
            return None

if __name__ == '__main__':
    converter = FootToMeterConverter()
    sample_feet = 10
    meters = converter.convert(sample_feet)
    print(f"{sample_feet} feet is equal to {meters} meters")