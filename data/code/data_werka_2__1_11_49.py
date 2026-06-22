CONVERSION_FACTOR = 2.20462

def kilograms_to_pounds(weights_kg):
    return [weight * CONVERSION_FACTOR for weight in weights_kg]

if __name__ == '__main__':
    sample_weights_kg = [35, 65, 95, 125]
    converted_weights_lb = kilograms_to_pounds(sample_weights_kg)
    print(converted_weights_lb)