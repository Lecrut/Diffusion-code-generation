def calculate_absolute_difference(weight1, weight2):
    if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
        raise ValueError("Both weights must be numbers.")
    return abs(weight1 - weight2)

if __name__ == '__main__':
    try:
        weight_a = 75.5
        weight_b = 68.3
        difference = calculate_absolute_difference(weight_a, weight_b)
        print(difference)
    except ValueError as e:
        print(e)