class WeightConverter:

    def kg_to_lb(self, value):
        return value * 2.20462

    def lb_to_kg(self, value):
        return value / 2.20462

    def g_to_kg(self, value):
        return value / 1000.0

    def kg_to_g(self, value):
        return value * 1000.0
if __name__ == '__main__':
    converter = WeightConverter()
    print(converter.kg_to_lb(1))
    print(converter.lb_to_kg(2.20462))
    print(converter.g_to_kg(1000))
    print(converter.kg_to_g(1))