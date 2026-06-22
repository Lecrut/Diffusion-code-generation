FEET_TO_INCHES_FACTOR = 12

def to_inches(feet):
    if not isinstance(feet, (int, float)):
        raise TypeError("Input must be a number")
    if feet < 0:
        raise ValueError("Input must be non-negative")
    return feet * FEET_TO_INCHES_FACTOR

class UnitConverter:
    def __init__(self):
        self.factor = FEET_TO_INCHES_FACTOR

    def convert(self, feet):
        return to_inches(feet)

if __name__ == '__main__':
    converter = UnitConverter()
    sample_feet = 10
    result = converter.convert(sample_feet)
    print(result)