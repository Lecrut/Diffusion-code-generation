class LengthConverter:
    INCHES_TO_CM = 2.54
    CM_TO_INCHES = 1 / INCHES_TO_CM

    @staticmethod
    def inches_to_cm(inches):
        return inches * LengthConverter.INCHES_TO_CM

    @staticmethod
    def cm_to_inches(cm):
        return cm * LengthConverter.CM_TO_INCHES

if __name__ == '__main__':
    print(LengthConverter.inches_to_cm(1))
    print(LengthConverter.inches_to_cm(0.5))
    print(LengthConverter.cm_to_inches(2.54))
    print(LengthConverter.cm_to_inches(12.7))