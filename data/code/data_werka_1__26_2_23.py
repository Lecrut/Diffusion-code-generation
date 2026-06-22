def threshold_generator(values, threshold):
    for value in values:
        if value > threshold:
            yield True

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    threshold_value = 25
    
    generator = threshold_generator(sample_values, threshold_value)
    
    for result in generator:
        print(result)