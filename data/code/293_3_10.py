class UnitConverter:
    def __init__(self):
        self.kg_to_lb_factor = 2.20462
        self.lb_to_kg_factor = 1 / 2.20462
        self.kg_to_oz_factor = 35.274
        self.oz_to_kg_factor = 1 / 35.274

    def kg_to_lb(self, kg):
        return kg * self.kg_to_lb_factor

    def lb_to_kg(self, lb):
        return lb * self.lb_to_kg_factor

    def kg_to_oz(self, kg):
        return kg * self.kg_to_oz_factor

    def oz_to_kg(self, oz):
        return oz * self.oz_to_kg_factor

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.kg_to_lb(1))
    print(converter.lb_to_kg(2.20462))
    print(converter.kg_to_oz(1))
    print(converter.oz_to_kg(35.274))