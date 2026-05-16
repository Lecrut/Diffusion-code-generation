def find_outliers(weights, lower_bound, upper_bound):
    outliers = []
    for weight in weights:
        if weight < lower_bound or weight > upper_bound:
            outliers.append(weight)
    return outliers
if __name__ == '__main__':
    data = [45, 55, 150, 200, 250, 30, 199, 50, 201, 100]
    lower_bound = 50
    upper_bound = 200
    result = find_outliers(data, lower_bound, upper_bound)
    print(result)