def threshold_generator(threshold, iterable):
    for value in iterable:
        if value > threshold:
            yield True

if __name__ == '__main__':
    sample_values = [10, 20, 5, 30, 25]
    threshold_value = 15
    result = list(threshold_generator(threshold_value, sample_values))
    print(result)