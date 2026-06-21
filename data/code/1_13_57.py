CONVERSION_FACTOR = 2.20462

def convert_weights_to_pounds(weights_kg):
    return [weight * CONVERSION_FACTOR for weight in weights_kg]

if __name__ == '__main__':
    sample_weights_kg = [1, 5, 10, 20]
    converted_weights_lb = convert_weights_to_pounds(sample_weights_kg)
    print(converted_weights_lb)