class WeightConverter:
    def __init__(self):
        self.conversion_factor = 1 / 28.3495

    def grams_to_ounces(self, weights_in_grams):
        return [weight * self.conversion_factor for weight in weights_in_grams]

if __name__ == '__main__':
    converter = WeightConverter()
    sample_weights_grams = [100, 200, 300]
    converted_weights_ounces = converter.grams_to_ounces(sample_weights_grams)
    print(converted_weights_ounces)