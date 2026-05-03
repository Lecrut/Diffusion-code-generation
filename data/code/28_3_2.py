def compare_to_threshold(data, threshold):
    for item in data:
        if item > threshold:
            yield True
if __name__ == '__main__':
    sample_list = [10, 5, 20, 3, 15]
    threshold_value = 12
    results = list(compare_to_threshold(sample_list, threshold_value))
    print(results)