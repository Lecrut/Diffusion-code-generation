class ConversionUtils:
    FEET_TO_MICROMETERS_FACTOR = 304800

    @staticmethod
    def feet_to_micrometers(feet):
        if not isinstance(feet, (int, float)) or feet < 0:
            raise ValueError("Input must be a non-negative number")
        return feet * ConversionUtils.FEET_TO_MICROMETERS_FACTOR

if __name__ == '__main__':
    print(ConversionUtils.feet_to_micrometers(1))
    print(ConversionUtils.feet_to_micrometers(5))
    print(ConversionUtils.feet_to_micrometers(10))