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
    sample_weights = [1.0, 2.0, 0.0]
    try:
        result = compute_weighted_average(sample_figures, sample_weights)
        print(f"Sample Figures: {sample_figures}")
        print(f"Sample Weights: {sample_weights}")
        print(f"Weighted Average: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    sample_figures_two = [5.0, 15.0]
    sample_weights_two = [3.0, 0.0]
    try:
        result_two = compute_weighted_average(sample_figures_two, sample_weights_two)
        print(f"\nSample Figures: {sample_figures_two}")
        print(f"Sample Weights: {sample_weights_two}")
        print(f"Weighted Average: {result_two}")
    except ValueError as e:
        print(f"Error: {e}")
    sample_all_zero_weights = [10.0, 20.0]
    sample_all_zero_weights_list = [0.0, 0.0]
    try:
        result_three = compute_weighted_average(sample_all_zero_weights, sample_all_zero_weights_list)
        print(f"\nSample Figures: {sample_all_zero_weights}")
        print(f"Sample Weights: {sample_all_zero_weights_list}")
        print(f"Weighted Average (All Zero Weights): {result_three}")
    except ValueError as e:
        print(f"Error: {e}")