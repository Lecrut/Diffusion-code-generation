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
    header = f"{'Original Value':<10} {'Unit':<5} {'Converted (kg)':<10}"
    print(header)
    print('-' * len(header))
    for value, unit, converted in weights:
        print(f"{value:<10.2f} {unit:<5} {converted:<10.2f}")

if __name__ == '__main__':
    sample_weights = ['70 kg', '154 lbs', '60 kg']
    converted_weights = convert_weights(sample_weights)
    print_table(converted_weights)