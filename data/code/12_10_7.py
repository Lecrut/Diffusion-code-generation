import statistics
def calculate_weighted_average(ratios, weights):
    if len(ratios) != len(weights):
        raise ValueError("Ratios and weights must have the same length")
    if not ratios:
        return 0.0
    weighted_sum = sum(r * w for r, w in zip(ratios, weights))
    total_weight = sum(weights)
    if total_weight == 0:
        raise ZeroDivisionError("Total weight cannot be zero")
    return weighted_sum / total_weight
if __name__ == '__main__':
    weight_ratios = [1.5, 2.5, 3.0]
    weights = [10, 5, 15]
    try:
        weighted_avg = calculate_weighted_average(weight_ratios, weights)
        print(weighted_avg)
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")