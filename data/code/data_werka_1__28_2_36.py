def compare_elements_to_threshold(elements, threshold):
    for element in elements:
        if element > threshold:
            yield True

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    threshold_value = 25
    result_generator = compare_elements_to_threshold(sample_list, threshold_value)
    for result in result_generator:
        print(result)