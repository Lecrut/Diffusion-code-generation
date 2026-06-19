def compare_to_threshold(threshold, values):
    for value in values:
        if value > threshold:
            yield True
        else:
            yield False

if __name__ == '__main__':
    threshold_value = 10
    sample_values = [5, 12, 7, 18, 3, 9]
    
    results = list(compare_to_threshold(threshold_value, sample_values))
    print(results)