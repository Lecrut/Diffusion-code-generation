class WeightConverter:
    GRAMS_TO_OUNCES = 28.3495

    @staticmethod
    def convert_to_ounces(grams):
        return [g / WeightConverter.GRAMS_TO_OUNCES for g in grams]

if __name__ == '__main__':
    sample_weights = [100, 200, 300]
    converter = WeightConverter()
    print(converter.convert_to_ounces(sample_weights))