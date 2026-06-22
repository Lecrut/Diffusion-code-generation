class DistanceConverter:
    INCH_TO_MM = 25.4

    @staticmethod
    def inches_to_millimeters(inches):
        if not isinstance(inches, (int, float)):
            raise ValueError('Invalid input. Use a number.')
        return inches * DistanceConverter.INCH_TO_MM
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.inches_to_millimeters(1))
    print(converter.inches_to_millimeters(0))
    print(converter.inches_to_millimeters(-1))