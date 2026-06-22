class Converter:
    INCHES_TO_CM = 2.54

    @staticmethod
    def inches_to_cm(inches):
        return inches * Converter.INCHES_TO_CM
if __name__ == '__main__':
    converter = Converter()
    print(converter.inches_to_cm(10))
    print(converter.inches_to_cm(1))