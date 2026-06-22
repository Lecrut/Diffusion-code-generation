KILOGRAMS_TO_POUNDS = 2.20462

def convert_weights(weights_kg):
    if not isinstance(weights_kg, list) or not all(isinstance(w, (int, float)) for w in weights_kg):
        raise ValueError("Input must be a list of numbers.")
    
    return [weight * KILOGRAMS_TO_POUNDS for weight in weights_kg]

if __name__ == '__main__':
    sample_weights = [1.5, 7, 15.2, 30]
    converted_weights = convert_weights(sample_weights)
    print(converted_weights)