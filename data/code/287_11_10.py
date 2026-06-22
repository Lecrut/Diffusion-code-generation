def convert_weights(weights):
    conversions = {
        'kg': 1,
        'lbs': 0.453592
    }
    converted_weights = []
    for weight in weights:
        value, unit = weight.split()
        value = float(value)
        if unit not in conversions:
            raise ValueError(f"Unsupported unit: {unit}")
        converted_weight = value * conversions[unit]
        converted_weights.append((value, unit, converted_weight))
    return converted_weights

def print_table(weights):
    headers = ["Original Value", "Unit", "Converted (kg)"]
    print("\t".join(headers))
    for weight in weights:
        print(f"\t{'\t'.join(map(str, weight))}")

if __name__ == '__main__':
    sample_weights = ['10 kg', '20 lbs', '5 kg']
    converted_weights = convert_weights(sample_weights)
    print_table(converted_weights)