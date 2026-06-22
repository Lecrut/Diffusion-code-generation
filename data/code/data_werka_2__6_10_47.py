def calculate_weight_difference(weight_a, weight_b):
    if not (isinstance(weight_a, (int, float)) and isinstance(weight_b, (int, float))):
        raise ValueError("Both weights must be numbers.")
    return abs(weight_a - weight_b)

if __name__ == '__main__':
    sample_weight1 = 80.5
    sample_weight2 = 70.3
    difference = calculate_weight_difference(sample_weight1, sample_weight2)
    print(difference)