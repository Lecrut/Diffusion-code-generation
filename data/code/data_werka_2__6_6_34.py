def calculate_weight_difference(weight1: float, weight2: float) -> float:
    if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
        raise ValueError("Both weights must be numbers.")
    return abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weight1 = 90.2
    sample_weight2 = 85.6
    try:
        difference = calculate_weight_difference(sample_weight1, sample_weight2)
        print(difference)
    except ValueError as e:
        print(e)