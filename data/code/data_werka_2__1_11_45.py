class WeightConverter:
    def __init__(self, weights_kg):
        self.weights_kg = weights_kg

    def kilograms_to_pounds(self, kilograms):
        return kilograms * 2.20462

    def convert_all_to_pounds(self):
        return [self.kilograms_to_pounds(weight) for weight in self.weights_kg]

if __name__ == '__main__':
    sample_weights_kg = [30, 65, 85, 130]
    converter = WeightConverter(sample_weights_kg)
    converted_weights_lb = converter.convert_all_to_pounds()
    print(converted_weights_lb)