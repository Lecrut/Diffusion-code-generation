class MassConverter:

    def __init__(self):
        self.conversion_factor = 0.035274

    def grams_to_ounces(self, grams: float) -> str:
        ounces = grams * self.conversion_factor
        return f'{ounces:.2f}'
if __name__ == '__main__':
    converter = MassConverter()
    print(converter.grams_to_ounces(100))