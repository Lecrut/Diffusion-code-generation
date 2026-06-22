def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

class WeightConverter:
    def __init__(self, weights_kg):
        self.weights_kg = weights_kg

    def convert_all(self):
        return [kilograms_to_pounds(weight) for weight in self.weights_kg]

    def max_weight_in_pounds(self):
        return kilograms_to_pounds(max(self.weights_kg))

if __name__ == '__main__':
    sample_weights_kg = [30, 60, 90, 120]
    converter = WeightConverter(sample_weights_kg)
    print(converter.convert_all())
    print(f"Maximum weight in pounds: {converter.max_weight_in_pounds()}")