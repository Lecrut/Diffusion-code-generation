FEET_PER_INCH = 12

def feet_to_inches(feet: float) -> float:
    return feet * FEET_PER_INCH

class UnitConverter:
    def __init__(self, factor: float) -> None:
        self.factor = factor

    def convert(self, value: float) -> float:
        return value * self.factor

if __name__ == '__main__':
    test_values = [3, 10.5, 0.25, 100]
    for val in test_values:
        print(feet_to_inches(val))
    converter = UnitConverter(FEET_PER_INCH)
    print(converter.convert(7))