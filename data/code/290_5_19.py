class MassConverter:

    def ounces_to_grams(self, ounces):
        return int(ounces * 28.3495)
if __name__ == '__main__':
    converter = MassConverter()
    print(converter.ounces_to_grams(1.0))
    print(converter.ounces_to_grams(2.5))