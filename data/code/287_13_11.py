def convert_to_kg(weight_str):
    if weight_str.endswith('kg'):
        return float(weight_str[:-2])
    elif weight_str.endswith('lbs'):
        return float(weight_str[:-3]) * 0.453592
    else:
        raise ValueError("Unsupported unit")

def calculate_average_weight(weights):
    total_kg = sum(convert_to_kg(weight) for weight in weights)
    average_kg = total_kg / len(weights)
    return round(average_kg, 2)

if __name__ == '__main__':
    sample_weights = ['70kg', '154lbs', '60kg']
    print(calculate_average_weight(sample_weights))