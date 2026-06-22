CONVERSION_FACTOR = 2.20462

def validate_weights(weights):
    if not all(isinstance(weight, (int, float)) and weight >= 0 for weight in weights):
        raise ValueError("All weights must be non-negative numbers")

def kilograms_to_pounds(weights_kg):
    validate_weights(weights_kg)
    return [weight * CONVERSION_FACTOR for weight in weights_kg]

if __name__ == '__main__':
    sample_weights_kg = [60, 80, 100, 120]
    converted_weights_lb = kilograms_to_pounds(sample_weights_kg)
    print(converted_weights_lb)