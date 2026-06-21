def calculate_absolute_difference(weight1, weight2):
    if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
        raise ValueError("Both weights must be numbers.")
    return abs(weight1 - weight2)

if __name__ == '__main__':
    try:
        sample_weight_a = 80.0
        sample_weight_b = 72.5
        difference = calculate_absolute_difference(sample_weight_a, sample_weight_b)
        print(difference)
    except ValueError as e:
        print(e)