class LengthComparator:
    def __init__(self, length1, unit1, length2, unit2):
        self.length1 = length1
        self.unit1 = unit1
        self.length2 = length2
        self.unit2 = unit2
        self.converted1 = self._convert_to_inches(length1, unit1)
        self.converted2 = self._convert_to_inches(length2, unit2)

    def _convert_to_inches(self, length, unit):
        if unit == "inches":
            return length
        elif unit == "feet":
            return length * 12
        elif unit == "yards":
            return length * 36
        elif unit == "centimeters":
            return length / 2.54
        elif unit == "meters":
            return length / 0.0254
        else:
            raise ValueError(f"Unknown unit: {unit}")

    def compare(self):
        if self.converted1 < self.converted2:
            return f"{self.length1} {self.unit1} is shorter than {self.length2} {self.unit2}"
        elif self.converted1 > self.converted2:
            return f"{self.length1} {self.unit1} is longer than {self.length2} {self.unit2}"
        else:
            return f"{self.length1} {self.unit1} is equal to {self.length2} {self.unit2}"

if __name__ == '__main__':
    comparator = LengthComparator(1, "feet", 12, "inches")
    print(comparator.compare())