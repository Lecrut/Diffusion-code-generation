def compare_to_threshold(input_list, threshold):
    for element in input_list:
        if element > threshold:
            yield True

if __name__ == '__main__':
    sample_list = [10, 20, 5, 30, 25]
    threshold_value = 15
    result = compare_to_threshold(sample_list, threshold_value)
    for value in result:
        print(value)