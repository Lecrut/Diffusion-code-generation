class UnitConverter:
    FEET_TO_INCHES_FACTOR = 12

    @staticmethod
    def convert_feet_to_inches(feet_value):
        if feet_value < 0:
            raise ValueError("Feet value cannot be negative")
        return feet_value * UnitConverter.FEET_TO_INCHES_FACTOR

if __name__ == '__main__':
    sample_feet = 10.75
    inches = UnitConverter.convert_feet_to_inches(sample_feet)
    print(inches)