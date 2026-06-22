def convert_to_kg(weight, unit):
    conversion_factors = {'kg': 1, 'lbs': 0.453592}
    return weight * conversion_factors[unit]

def calculate_average_weight(weights):
    total_weight = sum(convert_to_kg(weight, unit) for weight, unit in weights)
    average_weight = total_weight / len(weights)
    return round(average_weight, 2)

if __name__ == '__main__':
    sample_weights = [(80, 'kg'), (135, 'lbs'), (70, 'kg')]
    print(calculate_average_weight(sample_weights))