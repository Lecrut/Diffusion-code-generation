def weighted_average(measurements):
    total_weight = sum(weight for _, weight in measurements)
    if total_weight == 0:
        return 0
    weighted_sum = sum(value * weight for value, weight in measurements)
    return weighted_sum / total_weight

if __name__ == '__main__':
    sample_measurements = [(10, 2), (20, 3), (30, 5)]
    result = weighted_average(sample_measurements)
    print(result)