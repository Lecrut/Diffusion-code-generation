def threshold_generator(iterable, threshold):
    for value in iterable:
        if value > threshold:
            yield True

if __name__ == '__main__':
    sample_values = [10, 20, 5, 30, 25, 15]
    threshold_value = 18
    result = list(threshold_generator(sample_values, threshold_value))
    print(result)