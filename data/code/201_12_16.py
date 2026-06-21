def calculate_mean(values):
    if not all(isinstance(x, float) for x in values):
        raise TypeError("All elements in the iterable must be floats")
    
    total = sum(values)
    count = len(values)
    
    return total / count

if __name__ == '__main__':
    sample_values = [1.0, 2.5, 4.0, 6.75]
    mean_value = calculate_mean(sample_values)
    print(mean_value)