def compare_to_threshold(data, threshold):
    for item in data:
        if item > threshold:
            yield True
if __name__ == '__main__':
    input_list = [10, 25, 5, 40, 15]
    threshold_value = 20
    results = list(compare_to_threshold(input_list, threshold_value))
    print(results)