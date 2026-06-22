class UnitConverter:
    FEET_TO_INCHES_FACTOR = 12

    def convert(self, feet):
        if not isinstance(feet, (int, float)):
            raise TypeError("Input must be a number")
        return feet * self.FEET_TO_INCHES_FACTOR

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.convert(0))
    print(converter.convert(1))
    print(converter.convert(2.5))
    print(converter.convert(10))
    print(converter.convert(-3))