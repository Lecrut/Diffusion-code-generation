def threshold_generator(data, threshold):
    for item in data:
        if item > threshold:
            yield True
if __name__ == '__main__':
    sample_data = [1, 5, 10, 3, 15, 8]
    sample_threshold = 7
    generator = threshold_generator(sample_data, sample_threshold)
    results = list(generator)
    print(results)