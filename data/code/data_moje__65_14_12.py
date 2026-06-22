class LengthConverter:
    FEET_TO_INCHES_RATIO = 12

    @staticmethod
    def feet_to_inches(feet):
        return feet * LengthConverter.FEET_TO_INCHES_RATIO

if __name__ == '__main__':
    print(LengthConverter.feet_to_inches(5))
    print(LengthConverter.feet_to_inches(0))
    print(LengthConverter.feet_to_inches(10.5))
    print(LengthConverter.feet_to_inches(-3))