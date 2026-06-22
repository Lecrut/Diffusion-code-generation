class UnitConverter:
    def kg_to_lb(self, kg):
        return kg * 2.20462

    def lb_to_kg(self, lb):
        return lb / 2.20462

    def kg_to_oz(self, kg):
        return kg * 35.274

    def oz_to_kg(self, oz):
        return oz / 35.274

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.kg_to_lb(0.5))
    print(converter.lb_to_kg(1))
    print(converter.kg_to_oz(0.25))
    print(converter.oz_to_kg(8))