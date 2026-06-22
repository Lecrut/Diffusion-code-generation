class WeightConverter:
    POUNDS_TO_KG = 0.453592

    @staticmethod
    def convert_pounds_to_kg(pounds):
        kilograms = pounds * WeightConverter.POUNDS_TO_KG
        return "{:.2f}".format(kilograms)

if __name__ == '__main__':
    sample_pounds = [10, 20, 30]
    converter = WeightConverter()
    for pounds in sample_pounds:
        print(converter.convert_pounds_to_kg(pounds))