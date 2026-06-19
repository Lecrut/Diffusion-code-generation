def compare_to_threshold(elements, threshold):
    for element in elements:
        if element > threshold:
            yield True

if __name__ == '__main__':
    sample_list = [10, 20, 5, 30, 25]
    threshold_value = 15
    results = list(compare_to_threshold(sample_list, threshold_value))
    print(results)