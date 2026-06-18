def compute_weighted_average(figures, weights):
    if not figures or not weights:
        return 0.0
    total_weighted_sum = 0.0
    total_weight = 0.0
    for figure, weight in zip(figures, weights):
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
    print(f"Result 1: {result1}")
    sample_figures_2 = [50, 75]
    sample_weights_2 = [4, 0]
    result2 = compute_weighted_average(sample_figures_2, sample_weights_2)
    print(f"Result 2: {result2}")
    sample_figures_3 = [100]
    sample_weights_3 = [0]
    result3 = compute_weighted_average(sample_figures_3, sample_weights_3)
    print(f"Result 3: {result3}")
    sample_figures_4 = []
    sample_weights_4 = []
    result4 = compute_weighted_average(sample_figures_4, sample_weights_4)
    print(f"Result 4: {result4}")