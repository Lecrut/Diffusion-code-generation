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
    sample_weights = [1, 2, 3]
    result1 = compute_weighted_average(sample_figures, sample_weights)
    print(f"Weighted Average 1: {result1}")
    sample_figures_2 = [50, 100]
    sample_weights_2 = [4, 0]
    result2 = compute_weighted_average(sample_figures_2, sample_weights_2)
    print(f"Weighted Average 2: {result2}")
    sample_figures_3 = [100, 50]
    sample_weights_3 = [0, 0]
    result3 = compute_weighted_average(sample_figures_3, sample_weights_3)
    print(f"Weighted Average 3 (Zero Weights): {result3}")
    sample_figures_4 = [10, 20]
    sample_weights_4 = [5, 5]
    result4 = compute_weighted_average(sample_figures_4, sample_weights_4)
    print(f"Weighted Average 4: {result4}")