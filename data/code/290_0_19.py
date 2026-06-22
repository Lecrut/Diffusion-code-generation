class MassConverter:
    POUNDS_PER_KILOGRAM = 2.20462

    @staticmethod
    def kg_to_lb(kilograms):
        return kilograms * MassConverter.POUNDS_PER_KILOGRAM

if __name__ == '__main__':
    converter = MassConverter()
    print(converter.kg_to_lb(1))
    print(converter.kg_to_lb(5.5))
    print(converter.kg_to_lb(10))