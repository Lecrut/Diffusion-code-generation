def convert_to_kilograms(weights):
    conversion_factors = {
        'kg': 1,
        'g': 0.001,
        'lbs': 0.453592,
        'oz': 0.0283495,
        'tons': 1000
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
        "150 g",
        "220 lbs",
        "34 oz",
        "1 tons",
        "invalid input"
    ]
    
    print(convert_to_kilograms(sample_weights))