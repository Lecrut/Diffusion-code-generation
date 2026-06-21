def validate_weight(weight):
    if not isinstance(weight, (int, float)):
        raise ValueError("Weight must be a number.")

def calculate_weight_difference(weight1: float, weight2: float) -> float:
    validate_weight(weight1)
    validate_weight(weight2)
    return abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weight1 = 60.5
    sample_weight2 = 55.3
    try:
        difference = calculate_weight_difference(sample_weight1, sample_weight2)
        print(difference)
    except ValueError as e:
        print(e)