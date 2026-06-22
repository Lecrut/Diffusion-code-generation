class MassConverter:
    CONVERSION_FACTOR = 28.3495

    @staticmethod
    def grams_to_ounces(grams):
        return grams / MassConverter.CONVERSION_FACTOR

if __name__ == '__main__':
    mass_g = 2500
    result_oz = MassConverter.grams_to_ounces(mass_g)
    print(f"Input Mass: {mass_g} g")
    print(f"Converted Mass: {result_oz} oz")