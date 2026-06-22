def weighted_average(measurements):
    total_weighted_sum = 0.0
    total_weight = 0.0
    for value, category_weight in measurements:
        weighted_value = value * category_weight
        total_weighted_sum += weighted_value
        total_weight += category_weight
    if total_weight == 0:
        return 0.0
    return total_weighted_sum / total_weight

if __name__ == '__main__':
    measurements = [
        (10, 2),
        (20, 3),
        (30, 5)
    ]
    result = weighted_average(measurements)
    print(result)