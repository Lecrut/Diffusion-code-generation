def weighted_average(measurements, category_weights):
    total_weighted_value = sum(m * category_weights[c] for m, c in measurements)
    total_weight = sum(category_weights[c] for _, c in measurements)
    if total_weight == 0:
        return 0.0
    return total_weighted_value / total_weight

if __name__ == '__main__':
    sample_measurements = [(10.5, 'A'), (20.3, 'B'), (15.7, 'A'), (25.1, 'C')]
    sample_category_weights = {'A': 1, 'B': 2, 'C': 3}
    print(weighted_average(sample_measurements, sample_category_weights))