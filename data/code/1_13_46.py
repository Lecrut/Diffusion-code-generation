CONVERSION_RATE = 2.20462

def validate_weights(weights):
    if not isinstance(weights, list):
        raise ValueError("Input must be a list of weights.")
    for weight in weights:
        if not isinstance(weight, (int, float)):
            raise ValueError("All weights must be numbers.")

def kilograms_to_pounds(weights_kg):
    validate_weights(weights_kg)
    return [weight * CONVERSION_RATE for weight in weights_kg]

if __name__ == '__main__':
    sample_weights = [1.5, 2.5, 3.75, 4.0]
    converted_weights = kilograms_to_pounds(sample_weights)
    print(converted_weights)