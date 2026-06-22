class UnitConverter:
    INCHES_PER_FOOT = 12

    @staticmethod
    def convert_feet_to_inches(feet_value):
        return feet_value * UnitConverter.INCHES_PER_FOOT

if __name__ == '__main__':
    sample_feet = 12
    computed_inches = UnitConverter.convert_feet_to_inches(sample_feet)
    assert computed_inches == 144
    print(computed_inches)