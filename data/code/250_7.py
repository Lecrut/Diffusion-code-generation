def calculate_weighted_average(values, weights):
    if len(values) != len(weights):
        raise ValueError("Values and weights lists must have the same length")
    if not values:
        return 0
    weighted_sum = 0
    total_weight = 0
    for value, weight in zip(values, weights):
        weighted_sum += value * weight
        total_weight += weight
    if total_weight == 0:
        return 0
    return weighted_sum / total_weight
if __name__ == '__main__':
    scores = [10, 20, 30]
    weights = [1, 2, 3]
    result = calculate_weighted_average(scores, weights)
    print(result)