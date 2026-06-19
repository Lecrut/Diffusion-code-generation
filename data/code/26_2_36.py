def threshold_generator(threshold, iterable):
    for value in iterable:
        if value > threshold:
            yield True

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    threshold_value = 25
    result = list(threshold_generator(threshold_value, sample_values))
    print(result)