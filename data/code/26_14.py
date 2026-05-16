def threshold_generator(data, threshold):
    for item in data:
        if item > threshold:
            yield True
if __name__ == '__main__':
    sample_data = [1, 5, 2, 8, 3, 10, 4]
    sample_threshold = 5
    generator = threshold_generator(sample_data, sample_threshold)
    results = list(generator)
    print(results)