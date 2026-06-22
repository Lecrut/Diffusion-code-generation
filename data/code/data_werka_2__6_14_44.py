MAX_WEIGHT = 10000.0

def compute_weight_difference(weight1, weight2):
    if weight1 < 0 or weight2 < 0:
        raise ValueError("Weights cannot be negative")
    if weight1 > MAX_WEIGHT or weight2 > MAX_WEIGHT:
        raise ValueError(f"Weights cannot exceed {MAX_WEIGHT}")
    return abs(weight1 - weight2)

if __name__ == '__main__':
    try:
        weight1 = 5000.0
        weight2 = 3000.0
        difference = compute_weight_difference(weight1, weight2)
        print(difference)
    except ValueError as e:
        print(e)