CONVERSION_FACTOR = 2.20462

def validate_weights(weights):
    if not isinstance(weights, list):
        raise ValueError("Input must be a list")
    for weight in weights:
        if not isinstance(weight, (int, float)) or weight < 0:
            raise ValueError("All weights must be non-negative numbers")

def kilograms_to_pounds(kilograms):
    return [weight * CONVERSION_FACTOR for weight in kilograms]

if __name__ == '__main__':
    sample_weights_kg = [30, 65, 95, 130]
    validate_weights(sample_weights_kg)
    converted_weights_lb = kilograms_to_pounds(sample_weights_kg)
    print(converted_weights_lb)