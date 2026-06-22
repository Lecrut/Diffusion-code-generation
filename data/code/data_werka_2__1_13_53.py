CONVERSION_FACTORS = {
    'kg_to_lb': 2.20462
}

def convert_weights(weights_kg):
    conversion_factor = CONVERSION_FACTORS['kg_to_lb']
    return [weight * conversion_factor for weight in weights_kg]

if __name__ == '__main__':
    sample_weights = [1, 5, 10, 20]
    converted_weights = convert_weights(sample_weights)
    print(converted_weights)