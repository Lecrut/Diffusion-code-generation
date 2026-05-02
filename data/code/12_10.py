import statistics
def calculate_weighted_average(ratios, weights):
    if len(ratios) != len(weights):
        raise ValueError("Ratios and weights must have the same length")
    if not ratios:
        return 0.0
    weighted_sum = 0.0
    total_weight = 0.0
    for ratio, weight in zip(ratios, weights):
        weighted_sum += ratio * weight
        total_weight += weight
    if total_weight == 0:
        return 0.0
    return weighted_sum / total_weight
if __name__ == '__main__':
    weight_ratios = [1.5, 2.0, 0.5]
    weights = [10, 5, 15]
    try:
        weighted_avg = calculate_weighted_average(weight_ratios, weights)
        print(weighted_avg)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")