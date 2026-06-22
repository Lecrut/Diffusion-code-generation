def threshold_generator(threshold, sequence):
    for value in sequence:
        if value > threshold:
            yield True

if __name__ == '__main__':
    sample_threshold = 10
    sample_sequence = [5, 15, 20, 8, 30]
    result = list(threshold_generator(sample_threshold, sample_sequence))
    print(result)