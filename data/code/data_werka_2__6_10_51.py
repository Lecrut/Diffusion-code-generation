def compute_weight_difference(weight1, weight2):
    if not (isinstance(weight1, (int, float)) and isinstance(weight2, (int, float))):
        raise ValueError("Both weights must be numbers.")
    return abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weight1 = 70.8
    sample_weight2 = 65.4
    difference = compute_weight_difference(sample_weight1, sample_weight2)
    print(difference)