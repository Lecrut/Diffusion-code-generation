class FeetToMetersConverter:
    def __init__(self):
        self.factor = 0.3048

    def convert(self, feet):
        return feet * self.factor

if __name__ == '__main__':
    converter = FeetToMetersConverter()
    result = converter.convert(10)
    print(result)