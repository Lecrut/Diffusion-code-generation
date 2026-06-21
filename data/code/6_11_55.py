def calculate_weight_difference(weight1, weight2):
    if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
        raise ValueError("Both weights must be numbers")
    return abs(weight1 - weight2)

if __name__ == '__main__':
    try:
        weight1 = 70.3
        weight2 = 65.8
        difference = calculate_weight_difference(weight1, weight2)
        print(difference)
    except ValueError as e:
        print(e)