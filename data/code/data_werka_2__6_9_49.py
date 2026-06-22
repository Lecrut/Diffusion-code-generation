def validate_weight(weight):
    if not isinstance(weight, float):
        raise ValueError("Weight must be a float.")
    return weight

def calculate_absolute_difference(weight1, weight2):
    weight1 = validate_weight(weight1)
    weight2 = validate_weight(weight2)
    return abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weight_a = 80.0
    sample_weight_b = 75.3
    difference = calculate_absolute_difference(sample_weight_a, sample_weight_b)
    print(difference)