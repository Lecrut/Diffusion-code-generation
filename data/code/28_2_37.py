def compare_to_threshold(threshold, values):
    for value in values:
        if value > threshold:
            yield True

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    threshold_value = 25
    results = list(compare_to_threshold(threshold_value, sample_values))
    print(results)