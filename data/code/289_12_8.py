class DistanceConverter:
    INCHES_TO_CM = 2.54

    @staticmethod
    def to_cm(inches):
        return round(inches * DistanceConverter.INCHES_TO_CM, 1)
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.to_cm(10))
    print(converter.to_cm(3.5))
    print(converter.to_cm(7.62))