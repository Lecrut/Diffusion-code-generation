class OunceToGramConverter:

    def ounces_to_grams(self, ounces):
        return round(ounces * 28.3495, 0)
if __name__ == '__main__':
    converter = OunceToGramConverter()
    print(converter.ounces_to_grams(1))
    print(converter.ounces_to_grams(2.5))