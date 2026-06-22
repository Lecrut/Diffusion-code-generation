class LengthConverter:
    INCHES_PER_FOOT = 12

    @staticmethod
    def feet_to_inches(feet):
        return feet * LengthConverter.INCHES_PER_FOOT

if __name__ == '__main__':
    feet_amount = 10
    inches_result = LengthConverter.feet_to_inches(feet_amount)
    print(inches_result)