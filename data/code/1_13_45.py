class WeightConverter:
    CONVERSION_FACTOR = 2.20462

    def __init__(self, factor=CONVERSION_FACTOR):
        self.factor = factor

    def convert_kg_to_lb(self, weights_kg):
        return [weight * self.factor for weight in weights_kg]

if __name__ == '__main__':
    converter = WeightConverter()
    sample_weights_kg = [1.5, 2.3, 4.8, 10.2]
    converted_weights_lb = converter.convert_kg_to_lb(sample_weights_kg)
    print(converted_weights_lb)