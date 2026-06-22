class UnitConverter:
    KG_TO_LB = 2.20462
    LB_TO_KG = 1 / KG_TO_LB
    KG_TO_OZ = 35.274
    OZ_TO_KG = 1 / KG_TO_OZ

    @staticmethod
    def kg_to_lb(kg):
        return kg * UnitConverter.KG_TO_LB

    @staticmethod
    def lb_to_kg(lb):
        return lb * UnitConverter.LB_TO_KG

    @staticmethod
    def kg_to_oz(kg):
        return kg * UnitConverter.KG_TO_OZ

    @staticmethod
    def oz_to_kg(oz):
        return oz * UnitConverter.OZ_TO_KG

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.kg_to_lb(1))
    print(converter.lb_to_kg(2.20462))
    print(converter.kg_to_oz(1))
    print(converter.oz_to_kg(35.274))