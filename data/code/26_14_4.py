def threshold_generator(data, threshold):
    for item in data:
        if item > threshold:
            yield True
if __name__ == '__main__':
    sample_data = [1, 5, 3, 8, 2, 10, 4]
    sample_threshold = 5
    result_generator = threshold_generator(sample_data, sample_threshold)
    output_list = list(result_generator)
    print(output_list)