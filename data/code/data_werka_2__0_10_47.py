class LengthConversion:
    CM_TO_INCHES = 1 / 2.54

    @staticmethod
    def convert_cm_to_inches(cm):
        return cm * LengthConversion.CM_TO_INCHES

if __name__ == '__main__':
    sample_cm = 50
    inches = LengthConversion.convert_cm_to_inches(sample_cm)
    print(inches)