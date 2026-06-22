class MassConverter:
    def kg_to_lb(self, kilograms):
        return kilograms * 2.20462

if __name__ == '__main__':
    converter = MassConverter()
    print(converter.kg_to_lb(1))
    print(converter.kg_to_lb(5))
    print(converter.kg_to_lb(10))