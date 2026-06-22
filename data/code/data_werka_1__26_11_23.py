def threshold_generator(threshold, sequence):
    for value in sequence:
        if value > threshold:
            yield True

if __name__ == '__main__':
    sample_threshold = 10
    sample_sequence = [5, 12, 8, 15, 3, 20]
    
    generator = threshold_generator(sample_threshold, sample_sequence)
    for result in generator:
        print(result)