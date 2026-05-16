def find_outliers(weights, lower_bound, upper_bound):
    outliers = []
    for weight in weights:
        if weight < lower_bound or weight > upper_bound:
            outliers.append(weight)
    return outliers
if __name__ == '__main__':
    data = [45, 55, 150, 200, 210, 30, 199, 250, 49, 201]
    lower = 50
    upper = 200
    result = find_outliers(data, lower, upper)
    print(result)