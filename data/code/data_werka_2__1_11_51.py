CONVERSION_FACTOR = 2.20462

def kilograms_to_pounds(kilograms):
    if not isinstance(kilograms, (int, float)):
        raise ValueError("Input must be a number")
    return kilograms * CONVERSION_FACTOR

class WeightConverter:
    def __init__(self, weights_kg):
        self.weights_kg = weights_kg
    
    def convert_to_pounds(self):
        return [kilograms_to_pounds(weight) for weight in self.weights_kg]

if __name__ == '__main__':
    sample_weights_kg = [30, 65, 85, 130]
    converter = WeightConverter(sample_weights_kg)
    converted_weights_lb = converter.convert_to_pounds()
    print(converted_weights_lb)