class WeightConverter:
    CONVERSION_FACTOR = 2.20462

    @staticmethod
    def kilograms_to_pounds(kilograms):
        if not isinstance(kilograms, (int, float)):
            raise ValueError("Input must be a number")
        return kilograms * WeightConverter.CONVERSION_FACTOR

    def __init__(self, weights_kg):
        self.weights_kg = weights_kg

    def convert_weights(self):
        return [WeightConverter.kilograms_to_pounds(weight) for weight in self.weights_kg]

if __name__ == '__main__':
    sample_weights_kg = [30, 60, 90, 120]
    converter = WeightConverter(sample_weights_kg)
    converted_weights_lb = converter.convert_weights()
    print(converted_weights_lb)