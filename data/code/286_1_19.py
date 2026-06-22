class LengthConverter:
    conversion_factors = {
        'm': 1.0,
        'cm': 0.01,
        'km': 1000.0,
        'mm': 0.001
    }

    def __init__(self, value: float, from_unit: str):
        self.value = value
        self.from_unit = from_unit.lower()

    def to_meters(self) -> float:
        return self.value * self.conversion_factors.get(self.from_unit, 1.0)

if __name__ == '__main__':
    converter = LengthConverter(10, 'feet')
    meters = converter.to_meters()
    print(f"{converter.value} feet is {meters} meters")