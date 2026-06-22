class LengthComparator:
    def __init__(self, value1: float, unit1: str, value2: float, unit2: str):
        self.value1 = value1
        self.unit1 = unit1.lower()
        self.value2 = value2
        self.unit2 = unit2.lower()
        self.conversion_factors = {
            'meter': 1.0,
            'm': 1.0,
            'centimeter': 0.01,
            'cm': 0.01,
            'kilometer': 1000.0,
            'km': 1000.0,
            'inch': 0.0254,
            'in': 0.0254,
            'foot': 0.3048,
            'ft': 0.3048,
            'yard': 0.9144,
            'yd': 0.9144,
            'mile': 1609.34,
            'mi': 1609.34
        }

    def _to_meters(self, value: float, unit: str) -> float:
        factor = self.conversion_factors.get(unit)
        if factor is None:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * factor

    def compare(self) -> str:
        meters1 = self._to_meters(self.value1, self.unit1)
        meters2 = self._to_meters(self.value2, self.unit2)

        if meters1 > meters2:
            return f"{self.value1} {self.unit1} is greater than {self.value2} {self.unit2}"
        elif meters2 > meters1:
            return f"{self.value2} {self.unit2} is greater than {self.value1} {self.unit1}"
        else:
            return f"{self.value1} {self.unit1} is equal to {self.value2} {self.unit2}"

if __name__ == '__main__':
    c1 = LengthComparator(100, 'cm', 1, 'm')
    print(c1.compare())
    c2 = LengthComparator(5, 'ft', 2, 'm')
    print(c2.compare())
    c3 = LengthComparator(1, 'km', 1000, 'm')
    print(c3.compare())