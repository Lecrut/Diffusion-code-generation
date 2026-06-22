class WeightConverter:
    OUNCES_PER_POUND = 16

    def __init__(self, weights):
        self.weights = weights

    def convert_weights_to_ounces(self):
        return [weight * self.OUNCES_PER_POUND for weight in self.weights]

def combine_weights(weight_converter1, weight_converter2):
    combined_weights_in_ounces = weight_converter1.convert_weights_to_ounces() + \
                                 weight_converter2.convert_weights_to_ounces()
    return combined_weights_in_ounces

if __name__ == '__main__':
    weights_pounds = [10, 20, 30]
    weights_kg = [5, 10, 15]

    converter1 = WeightConverter(weights_pounds)
    converter2 = WeightConverter([weight * 2.20462 for weight in weights_kg])

    combined_weights = combine_weights(converter1, converter2)

    print(combined_weights)