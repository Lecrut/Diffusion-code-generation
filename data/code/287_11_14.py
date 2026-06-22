def convert_weights(weights):
    conversion_factors = {'kg': 1, 'lbs': 0.453592}
    converted_weights = []
    for weight in weights:
        value, unit = weight.split()
        value = float(value)
        converted_value = value * conversion_factors[unit]
        converted_weights.append((value, unit, converted_value))
    return converted_weights

def print_table(weights):
    headers = ["Original Value", "Unit", "Converted (kg)"]
    print("\t".join(headers))
    for weight in weights:
        print(f"{weight[0]:.2f}\t{weight[1]}\t{weight[2]:.2f}")

if __name__ == '__main__':
    sample_weights = ['50 kg', '100 lbs', '75 kg']
    converted_weights = convert_weights(sample_weights)
    print_table(converted_weights)