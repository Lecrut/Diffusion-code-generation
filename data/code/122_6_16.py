def validate_input(values):
    if not values:
        raise ValueError("The input list must not be empty")

def running_average_welford(values):
    validate_input(values)
    
    n = 0
    mean = 0.0
    M2 = 0.0
    
    for value in values:
        n += 1
        delta = value - mean
        mean += delta / n
        delta2 = value - mean
        M2 += delta * delta2
    
    if n < 2:
        raise ValueError("The input list must contain at least two elements")
    
    variance = M2 / (n - 1)
    std_deviation = variance ** 0.5
    
    return mean, std_deviation

if __name__ == '__main__':
    sample_values = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = running_average_welford(sample_values)
    print(result)