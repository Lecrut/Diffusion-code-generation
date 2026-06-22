class FootConverter:
    FOOT_TO_INCH_FACTOR = 12

    def __init__(self):
        self.conversion_factor = FootConverter.FOOT_TO_INCH_FACTOR

    def convert(self, feet):
        return feet * self.conversion_factor

if __name__ == '__main__':
    converter = FootConverter()
    print(converter.convert(3))
    print(converter.convert(10.0))
    print(converter.convert(0))
    print(converter.convert(1))