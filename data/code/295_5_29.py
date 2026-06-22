class ConversionUtils:
    INCHES_TO_CM_FACTOR = 2.54

    @staticmethod
    def inches_to_cm(inches):
        return inches * ConversionUtils.INCHES_TO_CM_FACTOR

if __name__ == '__main__':
    sample_inches = 10
    cm_value = ConversionUtils.inches_to_cm(sample_inches)
    print(f"{sample_inches} inches is {cm_value} cm")