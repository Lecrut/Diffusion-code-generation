class MassConverter:
    MG_TO_G_CONVERSION_FACTOR = 1000.0

    @staticmethod
    def mg_to_g(mg):
        return round(mg / MassConverter.MG_TO_G_CONVERSION_FACTOR, 3)

if __name__ == '__main__':
    converter = MassConverter()
    print(converter.mg_to_g(500))
    print(converter.mg_to_g(750))