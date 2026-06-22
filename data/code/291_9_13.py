class LengthComparator:
    def __init__(self):
        self.conversion_factor = 5.0292

    def convert_to_meters(self, length, unit):
        if unit == 'rods':
            return length * self.conversion_factor
        elif unit == 'meters':
            return length
        else:
            raise ValueError("Invalid unit")

    def compare_lengths(self, length1, unit1, length2, unit2):
        length1_m = self.convert_to_meters(length1, unit1)
        length2_m = self.convert_to_meters(length2, unit2)
        if length1_m < length2_m:
            return -1
        elif length1_m > length2_m:
            return 1
        else:
            return 0

if __name__ == '__main__':
    comparator = LengthComparator()
    print(comparator.compare_lengths(1, 'rods', 5.0292, 'meters'))
    print(comparator.compare_lengths(1, 'rods', 3, 'rods'))
    print(comparator.compare_lengths(2, 'rods', 10, 'meters'))