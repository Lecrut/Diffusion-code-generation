WEIGHT_THRESHOLD = 0.5

def calculate_weight_difference(weight1, weight2):
    if not (isinstance(weight1, (int, float)) and isinstance(weight2, (int, float))):
        raise ValueError("Both weights must be numbers.")
    difference = abs(weight1 - weight2)
    return round(difference, 1) if difference > WEIGHT_THRESHOLD else 0.0

if __name__ == '__main__':
    try:
        alice_weight = 82.3
        bob_weight = 79.8
        difference = calculate_weight_difference(alice_weight, bob_weight)
        print(f"Weight Difference: {difference}")
    except ValueError as e:
        print(e)