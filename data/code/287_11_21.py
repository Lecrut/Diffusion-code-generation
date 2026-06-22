def convert_weights(weight_list):
    conversion_factors = {'kg': 1, 'lbs': 0.453592}
    converted_weights = []
    for weight in weight_list:
        value, unit = weight.split()
        value = float(value)
        converted_weight = value * conversion_factors[unit]
        converted_weights.append((value, unit, converted_weight))
    return converted_weights

def print_table(weights):
    headers = ["Original Value", "Unit", "Converted (kg)"]
    print("\t".join(headers))
    for weight in weights:
        print("\t".join(map(str, weight)))

if __name__ == '__main__':
    sample_weights = ['80 kg', '120 lbs', '45 kg']
    converted_weights = convert_weights(sample_weights)
    print_table(converted_weights)