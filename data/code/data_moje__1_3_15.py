LOWER_LIMIT = 50
UPPER_LIMIT = 200

def is_outlier(weight_value):
    return weight_value < LOWER_LIMIT or weight_value > UPPER_LIMIT

def extract_outliers(dataset):
    return [entry for entry in dataset if is_outlier(entry)]

if __name__ == '__main__':
    sample_entries = [40, 50, 55, 100, 150, 200, 205, 250, 30, 0, -10, 1000]
    detected_outliers = extract_outliers(sample_entries)
    print(detected_outliers)