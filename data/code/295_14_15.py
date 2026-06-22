class UnitConverter:
    INCH_TO_CM = 2.54
    CM_TO_INCH = 0.393701

    @staticmethod
    def inches_to_cm(inches):
        return inches * UnitConverter.INCH_TO_CM

    @staticmethod
    def cm_to_inches(cm):
        return cm * UnitConverter.CM_TO_INCH

if __name__ == '__main__':
    print(f"1 inch to cm: {UnitConverter.inches_to_cm(1)}")
    print(f"1 cm to inches: {UnitConverter.cm_to_inches(1)}")