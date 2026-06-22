class UnitConverter:
    def kg_to_lb(self, kg):
        if not isinstance(kg, (int, float)) or kg < 0:
            raise ValueError("Invalid input for kilograms. Must be a non-negative number.")
        return kg * 2.20462

    def lb_to_kg(self, lb):
        if not isinstance(lb, (int, float)) or lb < 0:
            raise ValueError("Invalid input for pounds. Must be a non-negative number.")
        return lb / 2.20462

    def kg_to_oz(self, kg):
        if not isinstance(kg, (int, float)) or kg < 0:
            raise ValueError("Invalid input for kilograms. Must be a non-negative number.")
        return kg * 35.274

    def oz_to_kg(self, oz):
        if not isinstance(oz, (int, float)) or oz < 0:
            raise ValueError("Invalid input for ounces. Must be a non-negative number.")
        return oz / 35.274

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.kg_to_lb(1))
    print(converter.lb_to_kg(2.20462))
    print(converter.kg_to_oz(1))
    print(converter.oz_to_kg(35.274))