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
        return 0
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
    sample_figures_two = [100, 50]
    sample_weights_two = [5, 0]
    try:
        result_two = compute_weighted_average(sample_figures_two, sample_weights_two)
        print(f"\nSample Figures: {sample_figures_two}")
        print(f"Sample Weights: {sample_weights_two}")
        print(f"Weighted Average: {result_two}")
    except ValueError as e:
        print(f"Error: {e}")
    sample_figures_three = [10, 20]
    sample_weights_three = [0, 0]
    try:
        result_three = compute_weighted_average(sample_figures_three, sample_weights_three)
        print(f"\nSample Figures: {sample_figures_three}")
        print(f"Sample Weights: {sample_weights_three}")
        print(f"Weighted Average: {result_three}")
    except ValueError as e:
        print(f"Error: {e}")