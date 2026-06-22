class ConversionUtility:
    CM_TO_INCHES = 1 / 2.54

    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be a number.")
        self.value = value

    def to_inches(self):
        return self.value * ConversionUtility.CM_TO_INCHES

if __name__ == '__main__':
    sample_cm = 50
    converter = ConversionUtility(sample_cm)
    inches = converter.to_inches()
    print(inches)