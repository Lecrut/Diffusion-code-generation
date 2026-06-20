class LengthComparator:
    def compare(self, length1, unit1, length2, unit2):
        conversion_factors = {
            ('m', 'm'): 1,
            ('m', 'cm'): 100,
            ('m', 'mm'): 1000,
            ('m', 'in'): 39.3701,
            ('m', 'ft'): 3.28084,
            ('cm', 'm'): 0.01,
            ('cm', 'cm'): 1,
            ('cm', 'mm'): 10,
            ('cm', 'in'): 0.393701,
            ('cm', 'ft'): 0.0328084,
            ('mm', 'm'): 0.001,
            ('mm', 'cm'): 0.1,
            ('mm', 'mm'): 1,
            ('mm', 'in'): 0.0393701,
            ('mm', 'ft'): 0.00328084,
            ('in', 'm'): 0.0254,
            ('in', 'cm'): 2.54,
            ('in', 'mm'): 25.4,
            ('in', 'in'): 1,
            ('in', 'ft'): 0.0833333,
            ('ft', 'm'): 0.3048,
            ('ft', 'cm'): 30.48,
            ('ft', 'mm'): 304.8,
            ('ft', 'in'): 12,
            ('ft', 'ft'): 1,
        }
        normalized_length1 = length1 * conversion_factors.get((unit1, 'm'), 1)
        normalized_length2 = length2 * conversion_factors.get((unit2, 'm'), 1)
        if normalized_length1 > normalized_length2:
            return "greater than"
        elif normalized_length1 < normalized_length2:
            return "less than"
        else:
            return "equal to"

if __name__ == '__main__':
    comparator = LengthComparator()
    result = comparator.compare(1, 'm', 100, 'cm')
    print(result)
    result2 = comparator.compare(10, 'cm', 1, 'm')
    print(result2)
    result3 = comparator.compare(12, 'in', 1, 'ft')
    print(result3)