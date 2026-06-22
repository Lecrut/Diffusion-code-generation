CONVERSION_FACTOR = 2.20462

SAMPLE_WEIGHTS_KG = [0.0, 1.0, 10.0, 100.0, 1000.0, 72.57, 0.45359237]

def convert_kg_to_lbs(weights_kg):
    return [weight * CONVERSION_FACTOR for weight in weights_kg]

if __name__ == '__main__':
    result = convert_kg_to_lbs(SAMPLE_WEIGHTS_KG)
    print(result)