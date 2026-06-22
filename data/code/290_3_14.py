class MassConverter:
    def mg_to_g(self, milligrams):
        return round(milligrams / 1000.0, 3)

if __name__ == '__main__':
    converter = MassConverter()
    print(converter.mg_to_g(500))
    print(converter.mg_to_g(750))