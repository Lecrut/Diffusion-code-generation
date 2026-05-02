def find_outliers(weights, lower_bound, upper_bound):
    outliers = []
    for weight in weights:
        if weight < lower_bound or weight > upper_bound:
            outliers.append(weight)
    return outliers
if __name__ == '__main__':
    data = [45, 150, 210, 55, 199, 300, 49, 200, 100]
    lower = 50
    upper = 200
    result = find_outliers(data, lower, upper)
    print(result)