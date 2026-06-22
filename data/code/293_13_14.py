class WeightComparator:
    conversion_factors = {'kg': 1, 'lb': 0.453592}

    def convert_to_kg(self, weight, unit):
        return weight * self.conversion_factors[unit]

    def compare_weights(self, weight1, unit1, weight2, unit2):
        weight1_kg = self.convert_to_kg(weight1, unit1)
        weight2_kg = self.convert_to_kg(weight2, unit2)
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