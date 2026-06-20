def calculate_weighted_average(measurements):
    if not measurements:
        return 0.0
    total_weight = sum(weight for _, weight in measurements)
    if total_weight == 0:
        return 0.0
    weighted_sum = sum(measurement * weight for measurement, weight in measurements)
    return weighted_sum / total_weight

if __name__ == '__main__':
    data = [
        (10.0, 2.0),
        (20.0, 3.0),
        (30.0, 5.0)
    ]
    result = calculate_weighted_average(data)
    print(result)