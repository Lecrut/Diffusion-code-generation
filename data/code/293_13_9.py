class WeightComparator:
    CONVERSION_FACTORS = {'kg': 1, 'lb': 0.453592}

    @staticmethod
    def convert_to_kg(weight, unit):
        if unit not in WeightComparator.CONVERSION_FACTORS:
            raise ValueError('Invalid unit. Supported units are "kg" and "lb".')
        return weight * WeightComparator.CONVERSION_FACTORS[unit]

    @classmethod
    def compare_weights(cls, weight1, unit1, weight2, unit2):
        try:
            weight1_kg = cls.convert_to_kg(weight1, unit1)
            weight2_kg = cls.convert_to_kg(weight2, unit2)
        except ValueError as e:
            return str(e)
        if weight1_kg > weight2_kg:
            return f'{weight1} {unit1}'
        elif weight1_kg < weight2_kg:
            return f'{weight2} {unit2}'
        else:
            return 'Equal'

if __name__ == '__main__':
    comparator = WeightComparator()
    print(comparator.compare_weights(10, 'kg', 22, 'lb'))
    print(comparator.compare_weights(5, 'lb', 2.3, 'kg'))