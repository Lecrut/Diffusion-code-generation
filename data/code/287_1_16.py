class WeightConverter:
    OUNCES_PER_GRAM = 1 / 28.3495

    @staticmethod
    def grams_to_ounces(grams):
        return [g * WeightConverter.OUNCES_PER_GRAM for g in grams]

if __name__ == '__main__':
    sample_weights_grams = [100, 200, 300, 400]
    converted_weights_ounces = WeightConverter.grams_to_ounces(sample_weights_grams)
    print(converted_weights_ounces)