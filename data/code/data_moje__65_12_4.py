class LengthConverter:
    FOOT_TO_INCH = 12
    def __init__(self, base_unit, ratio):
        self.base_unit = base_unit
        self.ratio = ratio
    def convert(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("value must be numeric")
        return value * self.ratio
def main():
    converter = LengthConverter("feet", 12)
    feet_amount = 10
    inches = converter.convert(feet_amount)
    print(inches)
if __name__ == "__main__":
    main()