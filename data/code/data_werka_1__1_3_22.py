def find_outliers(weights, lower_bound=50, upper_bound=200):
    return [weight for weight in weights if weight < lower_bound or weight > upper_bound]

if __name__ == '__main__':
    sample_weights = [45, 60, 210, 75, 300, 90, 49, 201]
    outliers = find_outliers(sample_weights)
    print(outliers)