def compute_weight_difference(weight1, weight2):
    if weight1 < 0 or weight2 < 0:
        raise ValueError("Weights cannot be negative")
    return abs(weight1 - weight2)

if __name__ == '__main__':
    try:
        weight1 = 15.5
        weight2 = 10.2
        difference = compute_weight_difference(weight1, weight2)
        print(difference)
    except ValueError as e:
        print(e)