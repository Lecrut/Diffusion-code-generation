def validate_weight(weight):
    if not isinstance(weight, (int, float)):
        raise ValueError("Weight must be an integer or float.")
    return weight

def calculate_absolute_difference(weight1, weight2):
    validated_weight1 = validate_weight(weight1)
    validated_weight2 = validate_weight(weight2)
    return abs(validated_weight1 - validated_weight2)

if __name__ == '__main__':
    sample_weight_a = 75.5
    sample_weight_b = 68.3
    difference = calculate_absolute_difference(sample_weight_a, sample_weight_b)
    print(difference)