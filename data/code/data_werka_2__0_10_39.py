class UnitConverter:
    CM_TO_INCHES_FACTOR = 1 / 2.54

    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be a number.")
        self.value = value

    def convert(self, factor):
        return self.value * factor

if __name__ == '__main__':
    sample_cm = 50
    converter = UnitConverter(sample_cm)
    inches = converter.convert(UnitConverter.CM_TO_INCHES_FACTOR)
    print(inches)