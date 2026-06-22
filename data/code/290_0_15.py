class MassConverter:
    POUNDS_PER_KG = 2.20462

    @staticmethod
    def kg_to_pounds(kilograms):
        return kilograms * MassConverter.POUNDS_PER_KG

if __name__ == '__main__':
    converter = MassConverter()
    print(converter.kg_to_pounds(1))
    print(converter.kg_to_pounds(5.5))
    print(converter.kg_to_pounds(10))