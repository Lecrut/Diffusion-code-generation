def convert_to_kg(weight, unit):
    if unit == 'kg':
        return weight
    elif unit == 'lbs':
        return weight * 0.453592

def calculate_average_weight(weights):
    total = sum(convert_to_kg(weight, unit) for weight, unit in weights)
    average = total / len(weights)
    return round(average, 2)

if __name__ == '__main__':
    sample_weights = [(70, 'kg'), (154, 'lbs'), (60, 'kg')]
    print(calculate_average_weight(sample_weights))