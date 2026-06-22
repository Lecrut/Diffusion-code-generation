def convert_weights(weight_list):
    conversions = {
        'kg': 1,
        'lbs': 0.453592
    }
    
    converted_weights = []
    for weight in weight_list:
        value, unit = weight.split()
        value = float(value)
        converted_weight = value * conversions[unit]
        converted_weights.append((value, unit, converted_weight))
    
    return converted_weights

def print_table(weights):
    print(f"{'Original Value':<10} {'Unit':<5} {'Converted (kg)':<10}")
    for weight in weights:
        print(f"{weight[0]:<10.2f} {weight[1]:<5} {weight[2]:<10.2f}")

if __name__ == '__main__':
    sample_weights = ['70 kg', '154 lbs', '60 kg']
    converted_weights = convert_weights(sample_weights)
    print_table(converted_weights)