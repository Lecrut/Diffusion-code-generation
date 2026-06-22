class LengthComparator:
    INCHES_TO_FEET = 12

    @staticmethod
    def convert_to_feet(length_in_inches):
        return length_in_inches / LengthComparator.INCHES_TO_FEET

    @staticmethod
    def compare_lengths(length1, unit1, length2, unit2):
        if unit1 == 'inches':
            length1 = LengthComparator.convert_to_feet(length1)
            unit1 = 'feet'
        elif unit2 == 'inches':
            length2 = LengthComparator.convert_to_feet(length2)
            unit2 = 'feet'

        if length1 > length2:
            return (length1, unit1)
        else:
            return (length2, unit2)

if __name__ == '__main__':
    comparator = LengthComparator()
    result1 = comparator.compare_lengths(10, 'inches', 3, 'feet')
    print(f"Comparing 10 inches and 3 feet: {result1}")
    result2 = comparator.compare_lengths(72, 'inches', 6, 'feet')
    print(f"Comparing 72 inches and 6 feet: {result2}")