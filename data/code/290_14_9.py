class MassConverter:
    KILOGRAM_TO_POUND = 2.20462
    POUND_TO_KILOGRAM = 1 / KILOGRAM_TO_POUND

    @staticmethod
    def kg_to_lb(kg):
        return round(kg * MassConverter.KILOGRAM_TO_POUND, 2)

    @staticmethod
    def lb_to_kg(lb):
        return round(lb * MassConverter.POUND_TO_KILOGRAM, 2)

if __name__ == '__main__':
    converter = MassConverter()
    print(converter.kg_to_lb(1))
    print(converter.lb_to_kg(2.2))