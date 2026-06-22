class FeetToInchesConverter:
    INCHES_PER_FOOT = 12

    @staticmethod
    def convert(feet):
        return feet * FeetToInchesConverter.INCHES_PER_FOOT

if __name__ == '__main__':
    converter = FeetToInchesConverter()
    print(converter.convert(5))
    print(converter.convert(0))
    print(converter.convert(12.5))