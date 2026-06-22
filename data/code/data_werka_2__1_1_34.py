def convert_to_kilograms(weight_measurements):
    conversion_factors = {
        'kg': 1,
        'g': 0.001,
        'lbs': 0.453592,
        'oz': 0.0283495,
        'tons': 1000
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
        "220 lbs",
        "3.5 oz",
        "1 ton"
    ]
    print(convert_to_kilograms(sample_measurements))