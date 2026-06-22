INCHES_TO_CM = 2.54
CM_TO_INCHES = 1 / INCHES_TO_CM

class LengthConverter:
    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit.lower()

    def convert_to_cm(self) -> float:
        if self.unit == 'cm':
            return self.value
        elif self.unit == 'in':
            return self.value * INCHES_TO_CM
        else:
            raise ValueError(f"Unknown unit: {self.unit}")

    def convert_from_cm(self, value: float) -> float:
        if self.unit == 'cm':
            return value
        elif self.unit == 'in':
            return value * CM_TO_INCHES
        else:
            raise ValueError(f"Unknown unit: {self.unit}")

if __name__ == '__main__':
    converter = LengthConverter(5, 'in')
    print(f"{converter.value} inches is {converter.convert_to_cm()} cm")