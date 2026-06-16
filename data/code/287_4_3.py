import math
def calculate_average_weight(data):
    total_weight = 0.0
    total_value = 0.0
    conversion_factors = {}
    for weight, unit in data:
        if unit == 'kg':
            conversion_factors[unit] = 1.0
            total_weight += weight
        elif unit == 'lb':
            conversion_factors[unit] = 0.453592
            total_weight += weight * conversion_factors[unit]
        elif unit == 'g':
            conversion_factors[unit] = 0.001
            total_weight += weight * conversion_factors[unit]
        else:
            raise ValueError(f"Unknown unit: {unit}")
    if not data:
        return 0.0
    return total_weight / len(data)
if __name__ == '__main__':
    sample_data = [
        (10, 'kg'),
        (22, 'lb'),
        (500, 'g'),
        (15.5, 'kg')
    ]
    average = calculate_average_weight(sample_data)
    print(average)