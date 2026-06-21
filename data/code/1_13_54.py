CONVERSION_RATE = 2.20462

def kilograms_to_pounds(weights_kg):
    if not all(isinstance(weight, (int, float)) for weight in weights_kg):
        raise ValueError("All elements in the list must be numbers.")
    return [weight * CONVERSION_RATE for weight in weights_kg]

if __name__ == '__main__':
    sample_weights = [0.5, 2.3, 15.5, 40.0]
    try:
        converted_weights = kilograms_to_pounds(sample_weights)
        print(converted_weights)
    except ValueError as e:
        print(e)