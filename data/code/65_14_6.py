class UnitConverter:
    FEET_TO_INCHES_FACTOR = 12

    @staticmethod
    def feet_to_inches(feet):
        return feet * UnitConverter.FEET_TO_INCHES_FACTOR

if __name__ == '__main__':
    sample_values = [1, 3, 4.75, 0]
    for val in sample_values:
        print(UnitConverter.feet_to_inches(val))