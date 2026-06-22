class MassConverter:
    def kg_to_lb(self, kg):
        return round(kg * 2.20462, 2)

    def lb_to_kg(self, lb):
        return round(lb / 2.20462, 2)

if __name__ == '__main__':
    converter = MassConverter()
    print(converter.kg_to_lb(1))
    print(converter.lb_to_kg(2.2))
    print(converter.kg_to_lb(5))
    print(converter.lb_to_kg(11.02))