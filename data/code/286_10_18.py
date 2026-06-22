class Conversion:
    INCHES_TO_CM_FACTOR = 2.54

    @staticmethod
    def inches_to_cm(inches):
        return inches * Conversion.INCHES_TO_CM_FACTOR

if __name__ == '__main__':
    print(Conversion.inches_to_cm(1))
    print(Conversion.inches_to_cm(10))
    print(Conversion.inches_to_cm(100))