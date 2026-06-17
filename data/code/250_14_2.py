def calculate_weighted_average(scores, weights):
    total_weighted_sum = 0
    total_weight = 0
    if len(scores) != len(weights):
        raise ValueError("Scores and weights lists must have the same length")
    for score, weight in zip(scores, weights):
        total_weighted_sum += score * weight
        total_weight += weight
    if total_weight == 0:
        return 0
    else:
        return total_weighted_sum / total_weight
if __name__ == '__main__':
    scores_list = [85, 92, 78, 88]
    weights_list = [0.2, 0.3, 0.15, 0.35]
    weighted_avg = calculate_weighted_average(scores_list, weights_list)
    print(weighted_avg)