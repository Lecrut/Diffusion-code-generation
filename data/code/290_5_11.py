class MassConverter:
    OUNCE_TO_GRAM = 28.3495

    @staticmethod
    def convert_ounces_to_grams(ounces):
        return int(ounces * MassConverter.OUNCE_TO_GRAM)
if __name__ == '__main__':
    converter = MassConverter()
    print(converter.convert_ounces_to_grams(1))
    print(converter.convert_ounces_to_grams(0.5))
    print(converter.convert_ounces_to_grams(16))