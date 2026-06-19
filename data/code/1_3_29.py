def find_outliers(weights, lower_bound=50, upper_bound=200):
    outliers = [weight for weight in weights if weight < lower_bound or weight > upper_bound]
    return outliers

if __name__ == '__main__':
    sample_weights = [45, 60, 210, 180, 49, 201, 150, 300, 75]
    outliers = find_outliers(sample_weights)
    print(outliers)