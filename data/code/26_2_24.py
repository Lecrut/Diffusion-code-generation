def threshold_generator(iterable, threshold):
    for value in iterable:
        if value > threshold:
            yield True

if __name__ == '__main__':
    sample_data = [10, 20, 5, 30, 15]
    threshold_value = 18
    result = list(threshold_generator(sample_data, threshold_value))
    print(result)