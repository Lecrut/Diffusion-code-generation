def threshold_generator(iterable, threshold):
    for value in iterable:
        if value > threshold:
            yield True

if __name__ == '__main__':
    sample_data = [10, 20, 5, 30, 15]
    threshold_value = 15
    generator = threshold_generator(sample_data, threshold_value)
    
    for result in generator:
        print(result)