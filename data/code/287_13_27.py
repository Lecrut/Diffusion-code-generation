CONVERSION_FACTOR_LBS_TO_KG = 0.453592

def convert_to_kg(weight, unit):
    if unit == 'kg':
        return weight
    elif unit == 'lbs':
        return weight * CONVERSION_FACTOR_LBS_TO_KG
    else:
        raise ValueError("Unsupported unit")

def calculate_average_weight(weights):
    total_weight = sum(convert_to_kg(weight, unit) for weight, unit in weights)
    average_weight = total_weight / len(weights)
    return round(average_weight, 2)

if __name__ == '__main__':
    sample_weights = [(70, 'kg'), (154, 'lbs'), (60, 'kg')]
    print(calculate_average_weight(sample_weights))