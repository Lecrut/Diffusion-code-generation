def compute_weighted_average(figures: list[float], weights: list[float]) -> float:
    if len(figures) != len(weights):
        raise ValueError("The number of figures must match the number of weights.")
    total_weighted_sum = 0.0
    total_weight = 0.0
    for figure, weight in zip(figures, weights):
        if weight != 0:
            total_weighted_sum += figure * weight
            total_weight += weight
    if total_weight == 0:
        return 0.0
    else:
        return total_weighted_sum / total_weight
if __name__ == '__main__':
    sample_figures = [10.0, 20.0, 30.0]
    sample_weights = [1.0, 2.0, 0.5]
    try:
        result = compute_weighted_average(sample_figures, sample_weights)
        print(f"Sample Figures: {sample_figures}")
        print(f"Sample Weights: {sample_weights}")
        print(f"Weighted Average: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    sample_figures_zero = [100.0, 50.0]
    sample_weights_zero = [2.0, 0.0]
    try:
        result_zero = compute_weighted_average(sample_figures_zero, sample_weights_zero)
        print(f"\nTest with zero weight (Expected: 50.0): {result_zero}")
    except ValueError as e:
        print(f"Error in zero weight test: {e}")
    sample_figures_all_zero = [10.0, 20.0]
    sample_weights_all_zero = [0.0, 0.0]
    try:
        result_all_zero = compute_weighted_average(sample_figures_all_zero, sample_weights_all_zero)
        print(f"Test with all zero weights (Expected: 0.0): {result_all_zero}")
    except ValueError as e:
        print(f"Error in all zero weight test: {e}")