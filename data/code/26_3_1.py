def threshold_generator(data, threshold):
    for item in data:
        if item > threshold:
            yield True
if __name__ == '__main__':
    sample_data = [10, 5, 20, 3, 15, 25]
    sample_threshold = 12
    result_generator = threshold_generator(sample_data, sample_threshold)
    print("Testing with data:", sample_data)
    print("Testing with threshold:", sample_threshold)
    results = list(result_generator)
    print("Generated results:", results)