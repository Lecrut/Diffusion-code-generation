def compute_weight_difference(weight1, weight2):
    if weight1 < 0 or weight2 < 0:
        raise ValueError("Weights cannot be negative")
    return abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weights = [(15.5, 10.2), (0, 0), (-5, 10)]
    for weight1, weight2 in sample_weights:
        try:
            difference = compute_weight_difference(weight1, weight2)
            print(f"Difference between {weight1} and {weight2}: {difference}")
        except ValueError as e:
            print(f"Error with weights {weight1}, {weight2}: {e}")