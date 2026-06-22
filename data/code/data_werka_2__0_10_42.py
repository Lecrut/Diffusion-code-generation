class ConversionUtils:
    CM_TO_INCHES = 1 / 2.54

    @staticmethod
    def convert_cm_to_inches(cm):
        if not isinstance(cm, (int, float)):
            raise ValueError("Input must be a number.")
        return cm * ConversionUtils.CM_TO_INCHES

if __name__ == '__main__':
    sample_cm = 50
    inches = ConversionUtils.convert_cm_to_inches(sample_cm)
    print(inches)