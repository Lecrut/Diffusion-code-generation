class WeightConverter:
    def __init__(self):
        self.conversion_factor = 28.3495

    def grams_to_ounces(self, grams):
        return [g / self.conversion_factor for g in grams]

if __name__ == '__main__':
    converter = WeightConverter()
    sample_weights = [100, 200, 300]
    print(converter.grams_to_ounces(sample_weights))