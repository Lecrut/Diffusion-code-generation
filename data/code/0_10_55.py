class ConversionHelper:
    CM_TO_INCHES_FACTOR = 1 / 2.54

    @staticmethod
    def cm_to_inches(cm):
        if not isinstance(cm, (int, float)):
            raise ValueError("Input must be a number.")
        return cm * ConversionHelper.CM_TO_INCHES_FACTOR

if __name__ == '__main__':
    sample_cm = 50
    inches = ConversionHelper.cm_to_inches(sample_cm)
    print(inches)