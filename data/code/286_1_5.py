class FeetToMetersConverter:
    def __init__(self):
        self.conversion_factor = 0.3048

    def convert(self, feet):
        return feet * self.conversion_factor

if __name__ == '__main__':
    converter = FeetToMetersConverter()
    result = converter.convert(10)
    print(result)