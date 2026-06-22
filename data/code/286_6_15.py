class LengthConverter:
    INCHES_TO_CM = 2.54
    CM_TO_INCHES = 1 / INCHES_TO_CM

    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit.lower()

    def to_cm(self) -> float:
        if self.unit == 'in':
            return self.value * LengthConverter.INCHES_TO_CM
        elif self.unit == 'cm':
            return self.value
        else:
            raise ValueError(f'Unsupported unit: {self.unit}')

    def to_inches(self) -> float:
        if self.unit == 'in':
            return self.value
        elif self.unit == 'cm':
            return self.value * LengthConverter.CM_TO_INCHES
        else:
            raise ValueError(f'Unsupported unit: {self.unit}')
if __name__ == '__main__':
    converter = LengthConverter(10, 'in')
    print(converter.to_cm())
    converter = LengthConverter(25.4, 'cm')
    print(converter.to_inches())