def convert_to_kilograms(weight_measurements):
    conversion_factors = {
        'kg': 1,
        'g': 0.001,
        'lbs': 0.453592,
        'oz': 0.0283495,
        'tons': 1000
    }
    
    converted_weights = []
    for weight in weight_measurements:
        try:
            value, unit = weight.split()
            value = float(value)
            if unit not in conversion_factors:
                raise ValueError(f"Unknown unit: {unit}")
            converted_weight = value * conversion_factors[unit]
            converted_weights.append(converted_weight)
        except (ValueError, TypeError) as e:
            print(f"Error processing measurement '{weight}': {e}")
    
    return converted_weights

if __name__ == '__main__':
    sample_measurements = [
        "70 kg",
        "150 g",
        "200 lbs",
        "32 oz",
        "1 tons",
        "invalid measurement"
    ]
    
    print(convert_to_kilograms(sample_measurements))