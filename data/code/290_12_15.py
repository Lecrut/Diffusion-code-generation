class MassConverter:
    CONVERSION_FACTOR = 0.00220462

    @staticmethod
    def pounds_to_grams(pounds):
        return int(pounds / MassConverter.CONVERSION_FACTOR)

if __name__ == '__main__':
    converter = MassConverter()
    print(converter.pounds_to_grams(100))
    print(converter.pounds_to_grams(5000))