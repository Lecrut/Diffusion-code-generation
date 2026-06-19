class LengthComparator:

    def __init__(self, length1, unit1, length2, unit2):
        self.length1 = length1
        self.unit1 = unit1
        self.length2 = length2
        self.unit2 = unit2

    def compare(self):
        if self.unit1.lower() == 'meters' and self.unit2.lower() == 'centimeters':
            converted_length2 = self.length2 / 100
            return self.compare_values(self.length1, converted_length2)
        elif self.unit1.lower() == 'centimeters' and self.unit2.lower() == 'meters':
            converted_length1 = self.length1 / 100
            return self.compare_values(converted_length1, self.length2)
        elif self.unit1.lower() == self.unit2.lower():
            return self.compare_values(self.length1, self.length2)
        else:
            return 'Units are incompatible for comparison.'

    def compare_values(self, value1, value2):
        if value1 > value2:
            return f'{self.length1} {self.unit1} is greater than {self.length2} {self.unit2}.'
        elif value1 < value2:
            return f'{self.length1} {self.unit1} is less than {self.length2} {self.unit2}.'
        else:
            return f'{self.length1} {self.unit1} is equal to {self.length2} {self.unit2}.'
if __name__ == '__main__':
    comparator = LengthComparator(5, 'meters', 500, 'centimeters')
    print(comparator.compare())