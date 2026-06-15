def compute_weighted_average(figures, weights):
    if len(figures) != len(weights):
        raise ValueError("The number of figures must match the number of weights.")
    total_weighted_sum = 0
    total_weight = 0
    for figure, weight in zip(figures, weights):
        if weight != 0:
            total_weighted_sum += figure * weight
            total_weight += weight
    if total_weight == 0:
        return 0.0
    else:
        return total_weighted_sum / total_weight
if __name__ == '__main__':
    sample_figures = [10, 20, 30]
    sample_weights = [1, 2, 0]
    try:
        result = compute_weighted_average(sample_figures, sample_weights)
        print(f"Sample Figures: {sample_figures}")
        print(f"Sample Weights: {sample_weights}")
        print(f"Weighted Average: {result}")
    except ValueError as e:
        print(f"Error: {e}")