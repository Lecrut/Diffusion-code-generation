def calculate_weighted_average(measurements, category_weights):
    total_weight = sum(category_weights)
    weighted_sum = sum(m * w for m, w in zip(measurements, category_weights))
    return weighted_sum / total_weight if total_weight != 0 else 0

if __name__ == '__main__':
    measurements = [10, 20, 30]
    category_weights = [0.2, 0.3, 0.5]
    result = calculate_weighted_average(measurements, category_weights)
    print(result)