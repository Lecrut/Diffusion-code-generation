def validate_weight_data(weight_list):
    conversion_factors = {'kg': 1, 'lb': 0.453592}
    validated_weights = []
    for weight in weight_list:
        value, unit = weight.split()
        if not value.replace('.', '', 1).isdigit():
            raise ValueError("Invalid weight value")
        if unit not in conversion_factors:
            raise ValueError(f"Unknown unit: {unit}")
        validated_weights.append((float(value), unit))
    return validated_weights

def convert_weights(weight_list):
    validated_weights = validate_weight_data(weight_list)
    results = []
    for weight, unit in validated_weights:
        converted_weight = weight * (1 if unit == 'kg' else 0.453592)
        results.append((weight, unit, round(converted_weight, 2)))
    return results

def print_table(weights):
    headers = ["Original Value", "Unit", "Converted (kg)"]
    print("\t".join(headers))
    for weight in weights:
        print("\t".join(map(str, weight)))

if __name__ == '__main__':
    sample_weights = ['70 kg', '154 lb', '60 kg']
    converted_weights = convert_weights(sample_weights)
    print_table(converted_weights)