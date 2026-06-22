def convert_to_kilograms(weights):
    KILOGRAM = 1
    GRAM = 0.001
    POUND = 0.453592
    OUNCE = 0.0283495
    TON = 1000

    conversion_factors = {
        'kg': KILOGRAM,
        'g': GRAM,
        'lb': POUND,
        'oz': OUNCE,
        'ton': TON
    }

    converted_weights = []
    for weight in weights:
        try:
            value, unit = weight.split()
            value = float(value)
            if unit not in conversion_factors:
                raise ValueError(f"Unsupported unit: {unit}")
            converted_weight = value * conversion_factors[unit]
            converted_weights.append(converted_weight)
        except (ValueError, TypeError) as e:
            print(f"Error processing weight '{weight}': {e}")

    return converted_weights

if __name__ == '__main__':
    sample_weights = [
        "70 kg",
        "250 g",
        "150 lb",
        "8 oz",
        "3 ton"
    ]
    
    result = convert_to_kilograms(sample_weights)
    print(result)