def find_outliers(weight_data, lower_bound, upper_bound):
    outliers = []
    for entry in weight_data:
        if entry < lower_bound or entry > upper_bound:
            outliers.append(entry)
    return outliers

if __name__ == '__main__':
    sample_weights = [55.0, 45.0, 100.5, 201.0, 150.0, 30.0, 199.9, 200.1, 75.0]
    result = find_outliers(sample_weights, 50, 200)
    print(result)