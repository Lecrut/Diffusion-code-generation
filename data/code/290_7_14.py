class MassConverter:

    def convert_mass(self, mass_g):
        return int(mass_g * 1000)
if __name__ == '__main__':
    converter = MassConverter()
    print(converter.convert_mass(1))
    print(converter.convert_mass(1000))
    print(converter.convert_mass(0.5))
    print(converter.convert_mass(1000000000.0))