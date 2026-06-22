def validate_weight(weight):
    if not isinstance(weight, (int, float)):
        raise ValueError("Weight must be a number.")

def compute_weight_difference(weight1, weight2):
    validate_weight(weight1)
    validate_weight(weight2)
    return abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weight1 = 80.5
    sample_weight2 = 76.8
    try:
        difference = compute_weight_difference(sample_weight1, sample_weight2)
        print(difference)
    except ValueError as e:
        print(e)