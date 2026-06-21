MAX_WEIGHT = float('inf')
MIN_WEIGHT = 0

def compute_weight_difference(weight1, weight2):
    if not (MIN_WEIGHT <= weight1 <= MAX_WEIGHT) or not (MIN_WEIGHT <= weight2 <= MAX_WEIGHT):
        raise ValueError("Weights must be between 0 and infinity")
    return abs(weight1 - weight2)

if __name__ == '__main__':
    try:
        weight1 = 20.3
        weight2 = 5.8
        difference = compute_weight_difference(weight1, weight2)
        print(difference)
    except ValueError as e:
        print(e)