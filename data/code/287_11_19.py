def validate_weight_data(weight_list):
    if not weight_list:
        raise ValueError("Weight list cannot be empty")
    conversion_factors = {'kg': 1, 'lbs': 0.453592}
    for weight in weight_list:
        value, unit = weight.split()
        try:
            float(value)
        except ValueError:
            raise ValueError(f"Invalid weight value: {value}")
        if unit not in conversion_factors:
            raise ValueError(f"Unknown unit: {unit}")

def convert_weights(weight_list):
    validate_weight_data(weight_list)
    results = []
    for weight in weight_list:
        value, unit = weight.split()
        converted_weight = float(value) * {'kg': 1, 'lbs': 0.453592}[unit]
        results.append((float(value), unit, converted_weight))
    return results

def print_table(weights):
    headers = ["Original Value", "Unit", "Converted (kg)"]
    print("\t".join(headers))
    for weight in weights:
        print("\t".join(map(str, weight)))

if __name__ == '__main__':
    sample_weights = ['70 kg', '154 lbs', '60 kg']
    converted_weights = convert_weights(sample_weights)
    print_table(converted_weights)