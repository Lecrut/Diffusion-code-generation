class GramsToOuncesConverter:
    def grams_to_ounces(self, grams: float) -> str:
        ounces = grams * 0.035274
        return "{:.2f}".format(ounces)

if __name__ == '__main__':
    converter = GramsToOuncesConverter()
    print(converter.grams_to_ounces(16))
    print(converter.grams_to_ounces(1000))