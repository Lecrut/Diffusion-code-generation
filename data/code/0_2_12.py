class LengthConverter:
    INCHES_TO_CM_FACTOR = 2.54

    @staticmethod
    def inches_to_cm(inches):
        return inches * LengthConverter.INCHES_TO_CM_FACTOR

if __name__ == '__main__':
    values = [1, 12, 0.5, 100]
    for val in values:
        print(LengthConverter.inches_to_cm(val))