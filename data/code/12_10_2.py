import statistics
def calculate_weighted_average(ratios, weights):
    if len(ratios) != len(weights):
        raise ValueError("Ratios and weights must have the same length")
    if not ratios:
        return None
    weighted_sum = 0
    total_weight = 0
    for ratio, weight in zip(ratios, weights):
        weighted_sum += ratio * weight
        total_weight += weight
    if total_weight == 0:
        return None
    return weighted_sum / total_weight
if __name__ == '__main__':
    weight_ratios = [1.2, 0.8, 1.5, 0.5]
    weights = [10, 5, 15, 20]
    try:
        result = calculate_weighted_average(weight_ratios, weights)
        if result is not None:
            print(result)
        else:
            print("Calculation failed due to zero total weight or empty input.")
    except ValueError as e:
        print(f"Error: {e}")