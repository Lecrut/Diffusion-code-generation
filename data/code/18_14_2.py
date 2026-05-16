def threshold_generator(numbers, threshold):
    first_yield = False
    for number in numbers:
        if not first_yield:
            if number > threshold:
                yield True
            first_yield = True
        else:
            yield number > threshold
if __name__ == '__main__':
    sample_numbers = [10, 5, 20, 3]
    sample_threshold = 15
    generator = threshold_generator(sample_numbers, sample_threshold)
    results = list(generator)
    print(results)