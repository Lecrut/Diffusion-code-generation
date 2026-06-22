FEET_TO_INCHES_FACTOR = 12

def feet_to_inches(feet):
    if feet < 0:
        raise ValueError("Feet cannot be negative")
    return feet * FEET_TO_INCHES_FACTOR

class UnitConverter:
    def __init__(self, factor):
        self.factor = factor

    def convert(self, value):
        return value * self.factor

if __name__ == '__main__':
    print(feet_to_inches(10))
    print(feet_to_inches(3.25))
    converter = UnitConverter(FEET_TO_INCHES_FACTOR)
    print(converter.convert(7))