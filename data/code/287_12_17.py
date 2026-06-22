class WeightConverter:
    def __init__(self):
        self.conversion_factor = 0.035274

    def grams_to_ounces(self, weights_in_grams):
        return [weight * self.conversion_factor for weight in weights_in_grams]

if __name__ == '__main__':
    converter = WeightConverter()
    sample_weights = [100, 200, 300]
    print(converter.grams_to_ounces(sample_weights))