class DistanceConverter:
    INCHES_TO_CENTIMETERS = 2.54

    @staticmethod
    def to_centimeters(inches):
        return round(inches * DistanceConverter.INCHES_TO_CENTIMETERS, 1)
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.to_centimeters(1))
    print(converter.to_centimeters(72))
    print(converter.to_centimeters(3.5))