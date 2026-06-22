conversion_factors = {'kg': 1, 'lbs': 0.453592}

def convert_weights(weight_list):
    results = []
    for weight in weight_list:
        value, unit = weight.split()
        converted_weight = float(value) * conversion_factors[unit]
        results.append((weight, converted_weight))
    return results

def print_table(weights):
    headers = ["Original Value", "Converted (kg)"]
    print("\t".join(headers))
    for original, converted in weights:
        print(f"{original}\t{converted:.2f}")

if __name__ == '__main__':
    sample_weights = ['70 kg', '154 lbs', '60 kg']
    converted_weights = convert_weights(sample_weights)
    print_table(converted_weights)