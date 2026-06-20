def find_outlier_weights(weights, min_limit, max_limit):
    outliers = []
    for weight in weights:
        if weight < min_limit or weight > max_limit:
            outliers.append(weight)
    return outliers

if __name__ == '__main__':
    sample_weights = [45, 55, 60, 195, 205, 120, 10, 250, 99, 50]
    acceptable_min = 50
    acceptable_max = 200
    result = find_outlier_weights(sample_weights, acceptable_min, acceptable_max)
    print(result)