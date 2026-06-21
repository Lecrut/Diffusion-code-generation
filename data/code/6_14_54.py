def validate_weight(weight):
    if weight < 0:
        raise ValueError("Weights cannot be negative")
    return True

def compute_weight_difference(weight1, weight2):
    validate_weight(weight1)
    validate_weight(weight2)
    return abs(weight1 - weight2)

if __name__ == '__main__':
    try:
        weight1 = 20.3
        weight2 = 5.8
        difference = compute_weight_difference(weight1, weight2)
        print(difference)
    except ValueError as e:
        print(e)