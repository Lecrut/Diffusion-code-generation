def convert_weights(weight_list):
    conversion_factors = {
        'kg': 1,
        'lbs': 0.453592
    }
    converted_weights = []
    for weight in weight_list:
        value, unit = weight.split()
        value = float(value)
        if unit not in conversion_factors:
            raise ValueError(f"Unsupported unit: {unit}")
        converted_weight = value * conversion_factors[unit]
        converted_weights.append((value, unit, converted_weight))
    return converted_weights

def format_table(weights):
    headers = ["Original Value", "Unit", "Converted (kg)"]
    print("\t".join(headers))
    for weight in weights:
        print(f"{weight[0]:.2f}\t{weight[1]}\t{weight[2]:.2f}")

if __name__ == '__main__':
    sample_weights = ["70 kg", "154 lbs", "60 kg"]
    converted_weights = convert_weights(sample_weights)
    format_table(converted_weights)