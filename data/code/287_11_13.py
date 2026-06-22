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
        converted_weights.append((weight, f"{converted_weight:.2f} kg"))
    return converted_weights

if __name__ == '__main__':
    sample_weights = ['100 kg', '220 lbs', '50 kg']
    result = convert_weights(sample_weights)
    print("Original Weight\tConverted Weight")
    for original, converted in result:
        print(f"{original}\t{converted}")