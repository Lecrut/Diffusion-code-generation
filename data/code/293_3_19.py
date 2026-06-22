class UnitConverter:
    conversion_factors = {
        'kg_to_lb': 2.20462,
        'lb_to_kg': 1 / 2.20462,
        'kg_to_oz': 35.274,
        'oz_to_kg': 1 / 35.274
    }

    def kg_to_lb(self, kg):
        return self._convert(kg, 'kg_to_lb')

    def lb_to_kg(self, lb):
        return self._convert(lb, 'lb_to_kg')

    def kg_to_oz(self, kg):
        return self._convert(kg, 'kg_to_oz')

    def oz_to_kg(self, oz):
        return self._convert(oz, 'oz_to_kg')

    def _convert(self, value, factor_key):
        return value * self.conversion_factors[factor_key]

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.kg_to_lb(1))
    print(converter.lb_to_kg(2.20462))
    print(converter.kg_to_oz(1))
    print(converter.oz_to_kg(35.274))