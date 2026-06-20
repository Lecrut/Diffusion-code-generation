def find_outlier_measurements(measurements, lower_bound=50, upper_bound=200):
    return [
        m for m in measurements
        if m < lower_bound or m > upper_bound
    ]

if __name__ == '__main__':
    sample_weights = [45, 75, 150, 205, 199, 50, 200, 10, 500]
    outliers = find_outlier_measurements(sample_weights)
    print(outliers)