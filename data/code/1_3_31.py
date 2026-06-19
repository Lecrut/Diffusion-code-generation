def find_outliers(data, lower_bound, upper_bound):
    return [x for x in data if x < lower_bound or x > upper_bound]

if __name__ == '__main__':
    sample_data = [45, 60, 210, 78, 49, 201, 150, 50, 199, 200]
    lower_limit = 50
    upper_limit = 200
    outliers = find_outliers(sample_data, lower_limit, upper_limit)
    print(outliers)