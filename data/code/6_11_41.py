def validate_weights(weight1, weight2):
    if not (isinstance(weight1, (int, float)) and isinstance(weight2, (int, float))):
        raise ValueError("Both weights must be numbers")

def calculate_weight_difference(weight1, weight2):
    validate_weights(weight1, weight2)
    return abs(weight1 - weight2)

if __name__ == '__main__':
    try:
        weight1 = 70.2
        weight2 = 63.8
        difference = calculate_weight_difference(weight1, weight2)
        print(difference)
    except ValueError as e:
        print(e)