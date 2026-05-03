def find_outliers(weights, lower_bound, upper_bound):
    outliers = []
    for weight in weights:
        if weight < lower_bound or weight > upper_bound:
            outliers.append(weight)
    return outliers
if __name__ == '__main__':
    data = [45.5, 150.0, 210.2, 55.0, 300.1, 99.9, 49.9, 200.0, 200.1]
    lower = 50
    upper = 200
    result = find_outliers(data, lower, upper)
    print(result)