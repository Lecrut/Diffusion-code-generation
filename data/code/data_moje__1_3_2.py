def filter_outlier_weights(weights, min_limit, max_limit):
    return [weight for weight in weights if weight < min_limit or weight > max_limit]

if __name__ == '__main__':
    sample_data = [45, 55, 100, 199, 201, 50, 200, 49, 250, 150]
    result = filter_outlier_weights(sample_data, 50, 200)
    print(result)