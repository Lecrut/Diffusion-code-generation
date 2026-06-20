def compute_weighted_mean(data):
    numerator = 0.0
    denominator = 0.0
    for value, weight in data:
        numerator += value * weight
        denominator += weight
    if denominator == 0:
        return 0.0
    return numerator / denominator

if __name__ == '__main__':
    sample_data = [
        (5.0, 1),
        (10.0, 2),
        (15.0, 3)
    ]
    output = compute_weighted_mean(sample_data)
    print(output)