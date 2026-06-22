class MassConverter:
    def __init__(self):
        self.conversion_factor = 28.3495

    def grams_to_ounces(self, grams):
        return grams / self.conversion_factor

if __name__ == '__main__':
    converter = MassConverter()
    mass_g = 1000
    result_oz = converter.grams_to_ounces(mass_g)
    print(f"Input Mass: {mass_g} g")
    print(f"Converted Mass: {result_oz} oz")