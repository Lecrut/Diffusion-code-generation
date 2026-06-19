def compare_to_threshold(input_list, threshold):
    for element in input_list:
        if element > threshold:
            yield True
        else:
            yield False

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    threshold_value = 25
    results = list(compare_to_threshold(sample_list, threshold_value))
    print(results)