def threshold_generator(iterable, threshold):
    for value in iterable:
        if value > threshold:
            yield True

if __name__ == '__main__':
    SAMPLE_VALUES = [5, 15, 25, 35, 45]
    THRESHOLD_VALUE = 30
    generator = threshold_generator(SAMPLE_VALUES, THRESHOLD_VALUE)
    for result in generator:
        print(result)