def calculate_weighted_average(scores, weights):
    total_weighted_sum = 0
    total_weight = 0
    for score, weight in zip(scores, weights):
        total_weighted_sum += score * weight
        total_weight += weight
    if total_weight == 0:
        return 0
    return total_weighted_sum / total_weight
if __name__ == '__main__':
    sample_scores = [85, 92, 78, 88]
    sample_weights = [0.2, 0.3, 0.15, 0.35]
    weighted_avg = calculate_weighted_average(sample_scores, sample_weights)
    print(weighted_avg)