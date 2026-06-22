class UnitConverter:
    def kg_to_lb(self, kg):
        self.validate_kg(kg)
        return kg * 2.20462

    def lb_to_kg(self, lb):
        self.validate_lb(lb)
        return lb / 2.20462

    def kg_to_oz(self, kg):
        self.validate_kg(kg)
        return kg * 35.274

    def oz_to_kg(self, oz):
        self.validate_oz(oz)
        return oz / 35.274

    def validate_kg(self, kg):
        if not isinstance(kg, (int, float)) or kg < 0:
            raise ValueError("Kilograms must be a non-negative number")

    def validate_lb(self, lb):
        if not isinstance(lb, (int, float)) or lb < 0:
            raise ValueError("Pounds must be a non-negative number")

    def validate_oz(self, oz):
        if not isinstance(oz, (int, float)) or oz < 0:
            raise ValueError("Ounces must be a non-negative number")

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.kg_to_lb(1))
    print(converter.lb_to_kg(2.20462))
    print(converter.kg_to_oz(1))
    print(converter.oz_to_kg(35.274))