def validate_weight(weight):
    if not isinstance(weight, (int, float)):
        raise ValueError("Weight must be an integer or float.")

def calculate_absolute_difference(weight1, weight2):
    validate_weight(weight1)
    validate_weight(weight2)
    return abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weight1 = 70.0
    sample_weight2 = 65.4
    try:
        difference = calculate_absolute_difference(sample_weight1, sample_weight2)
        print(difference)
    except ValueError as e:
        print(e)