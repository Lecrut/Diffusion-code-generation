CONVERSION_FACTOR = 2.20462

def convert_kilograms_to_pounds(weights_kg):
    return [weight * CONVERSION_FACTOR for weight in weights_kg]

class WeightConverter:
    def __init__(self, weights_kg):
        self.weights_kg = weights_kg
    
    def get_converted_weights(self):
        return convert_kilograms_to_pounds(self.weights_kg)
    
    def print_converted_weights(self):
        converted_weights = self.get_converted_weights()
        for kg, lb in zip(self.weights_kg, converted_weights):
            print(f"{kg} kg is {lb:.2f} lbs")

if __name__ == '__main__':
    sample_weights_kg = [30, 65, 85, 130]
    converter = WeightConverter(sample_weights_kg)
    converter.print_converted_weights()