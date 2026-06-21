def calculate_weight_difference(weight1, weight2):
    if not (isinstance(weight1, (int, float)) and isinstance(weight2, (int, float))):
        raise ValueError("Both weights must be numbers")
    return abs(weight1 - weight2)

if __name__ == '__main__':
    try:
        weight1 = 90.7
        weight2 = 85.4
        difference = calculate_weight_difference(weight1, weight2)
        print(difference)
    except ValueError as e:
        print(e)