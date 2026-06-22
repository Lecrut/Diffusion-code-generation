def validate_weight(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Weight must be a number")

def calculate_weight_difference(weight1, weight2):
    validate_weight(weight1)
    validate_weight(weight2)
    return abs(weight1 - weight2)

if __name__ == '__main__':
    try:
        weight1 = 70.2
        weight2 = 65.8
        difference = calculate_weight_difference(weight1, weight2)
        print(difference)
    except ValueError as e:
        print(e)