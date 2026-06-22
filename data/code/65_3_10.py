class LengthConverter:
    FEET_TO_INCHES = 12

    @staticmethod
    def convert(feet):
        return feet * LengthConverter.FEET_TO_INCHES

if __name__ == '__main__':
    sample_feet = 3.25
    inches = LengthConverter.convert(sample_feet)
    print(inches)