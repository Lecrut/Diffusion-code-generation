def convert_weights(raw_weights):
    conversion_factors = {'kg': 1, 'lbs': 0.453592}
    results = []
    for weight, unit in raw_weights:
        if unit == 'kg':
            converted_weight = weight
        elif unit == 'lbs':
            converted_weight = weight * conversion_factors[unit]
        else:
            raise ValueError(f"Unknown unit: {unit}")
        results.append((weight, unit, converted_weight))
    return results

def print_table(weights):
    headers = ["Original Value", "Unit", "Converted (kg)"]
    print("\t".join(headers))
    for weight in weights:
        print("\t".join(map(str, weight)))

if __name__ == '__main__':
    raw_data = [
        ("70", "kg"),
        ("154", "lbs"),
        ("60", "kg")
    ]
    converted_weights = convert_weights(raw_data)
    print_table(converted_weights)