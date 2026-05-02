def threshold_generator(numbers, threshold):
    first_yielded = False
    for number in numbers:
        if not first_yielded:
            if number > threshold:
                yield True
            first_yielded = True
        else:
            yield number > threshold
if __name__ == '__main__':
    sample_numbers = [10, 5, 12, 3]
    sample_threshold = 7
    generator = threshold_generator(sample_numbers, sample_threshold)
    results = list(generator)
    print(results)