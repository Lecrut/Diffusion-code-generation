def convert_weights(weights):
    conversions = {'kg': 1, 'lbs': 0.453592}
    converted_weights = []
    for weight in weights:
        value, unit = weight.split()
        converted_weight = float(value) * conversions[unit]
        converted_weights.append((value, unit, f"{converted_weight:.2f} kg"))
    return converted_weights

def print_table(weights):
    headers = ["Original Value", "Unit", "Converted Weight"]
    max_widths = [max(len(header), len(str(max([len(w[0]) for w in weights])))) for header in headers]
    format_string = ' | '.join(f"{{:<{width}}}" for width in max_widths)
    print(format_string.format(*headers))
    print('-' * sum(max_widths) + '-' * (len(headers) - 1))
    for weight in weights:
        print(format_string.format(*weight))

if __name__ == '__main__':
    sample_weights = ["50 kg", "100 lbs", "75 kg"]
    converted_weights = convert_weights(sample_weights)
    print_table(converted_weights)