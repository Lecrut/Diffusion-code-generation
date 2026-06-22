class UnitConverter:
    KG_TO_LB = 2.20462
    LB_TO_KG = 1 / 2.20462
    KG_TO_OZ = 35.274
    OZ_TO_KG = 1 / 35.274

    def kg_to_lb(self, kg):
        return kg * self.KG_TO_LB

    def lb_to_kg(self, lb):
        return lb * self.LB_TO_KG

    def kg_to_oz(self, kg):
        return kg * self.KG_TO_OZ

    def oz_to_kg(self, oz):
        return oz * self.OZ_TO_KG

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.kg_to_lb(1))
    print(converter.lb_to_kg(2.20462))
    print(converter.kg_to_oz(1))
    print(converter.oz_to_kg(35.274))