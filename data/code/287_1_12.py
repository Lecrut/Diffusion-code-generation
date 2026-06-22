class WeightConverter:
    OUNCES_PER_GRAM = 1 / 28.3495

    @staticmethod
    def grams_to_ounces(grams):
        return [g * WeightConverter.OUNCES_PER_GRAM for g in grams]

if __name__ == '__main__':
    weights_in_grams = [100, 200, 300, 400]
    weights_in_ounces = WeightConverter.grams_to_ounces(weights_in_grams)
    print(weights_in_ounces)