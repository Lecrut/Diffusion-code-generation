class LengthComparator:
    def __init__(self, length1: float, unit1: str, length2: float, unit2: str):
        self.length1 = length1
        self.unit1 = unit1
        self.length2 = length2
        self.unit2 = unit2

    def compare(self) -> str:
        if self.unit1 == 'cm' and self.unit2 == 'cm':
            return f"{min(self.length1, self.length2)} cm"
        elif self.unit1 == 'm' and self.unit2 == 'cm':
            length1_cm = self.length1 * 100
            return f"{min(length1_cm, self.length2)} cm" if length1_cm < self.length2 else f"{self.length2} {self.unit2}"
        elif self.unit1 == 'cm' and self.unit2 == 'm':
            length2_cm = self.length2 * 100
            return f"{min(self.length1, length2_cm)} cm" if self.length1 < length2_cm else f"{self.length2} {self.unit2}"
        else:
            raise ValueError("Unsupported units")

if __name__ == '__main__':
    comparator1 = LengthComparator(50, 'cm', 3, 'm')
    print(comparator1.compare())
    comparator2 = LengthComparator(2.5, 'm', 250, 'cm')
    print(comparator2.compare())