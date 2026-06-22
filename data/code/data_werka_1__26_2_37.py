def value_above_threshold(iterable, threshold):
    for value in iterable:
        if value > threshold:
            yield True

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    threshold_value = 25
    generator = value_above_threshold(sample_values, threshold_value)
    for result in generator:
        print(result)