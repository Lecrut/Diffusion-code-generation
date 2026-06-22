def compute_weight_difference(weight1, weight2):
    if weight1 < 0 or weight2 < 0:
        raise ValueError("Weights cannot be negative")
    return abs(weight1 - weight2)

if __name__ == '__main__':
    try:
        sample_weight1 = 20.0
        sample_weight2 = 5.3
        difference = compute_weight_difference(sample_weight1, sample_weight2)
        print(f"The weight difference is: {difference}")
    except ValueError as e:
        print(e)