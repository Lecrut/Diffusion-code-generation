class LengthConverter:
    CM_TO_INCHES_FACTOR = 1 / 2.54

    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be a number.")
        self.value = value

    def convert_to_inches(self):
        return self.value * self.CM_TO_INCHES_FACTOR

if __name__ == '__main__':
    sample_cm = 50
    converter = LengthConverter(sample_cm)
    inches = converter.convert_to_inches()
    print(inches)