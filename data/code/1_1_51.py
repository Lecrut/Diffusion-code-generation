def convert_to_kilograms(weight_measurements):
    conversion_factors = {
        'kg': 1,
        'g': 0.001,
        'lb': 0.453592,
        'oz': 0.0283495,
        'ton': 1000
    }
    
    converted_weights = []
    for measurement in weight_measurements:
        try:
            value, unit = measurement.split()
            value = float(value)
            if unit not in conversion_factors:
                raise ValueError(f"Unsupported unit: {unit}")
            converted_weight = value * conversion_factors[unit]
            converted_weights.append(converted_weight)
        except (ValueError, TypeError) as e:
            print(f"Error processing measurement '{measurement}': {e}")
    
    return converted_weights

if __name__ == '__main__':
    sample_measurements = [
        "70 kg",
        "150 g",
        "160 lb",
        "32 oz",
        "0.5 ton",
        "invalid 100"
    ]
    print(convert_to_kilograms(sample_measurements))