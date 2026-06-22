def calculate_weight_difference(weight1, weight2):
    if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
        raise ValueError("Both weights must be numbers.")
    return abs(weight1 - weight2)

if __name__ == '__main__':
    try:
        weight_a = 85.0
        weight_b = 79.2
        difference = calculate_weight_difference(weight_a, weight_b)
        print(difference)
    except ValueError as e:
        print(e)