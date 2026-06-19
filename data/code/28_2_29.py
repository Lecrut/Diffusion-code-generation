def compare_to_threshold(input_list, threshold):
    for element in input_list:
        yield element > threshold

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    threshold_value = 25
    result_generator = compare_to_threshold(sample_list, threshold_value)
    for comparison_result in result_generator:
        print(comparison_result)