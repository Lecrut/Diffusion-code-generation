MEAN_CALCULATION_EPSILON = 1e-09

def calculate_mean(numbers):
    if not all((isinstance(num, float) for num in numbers)):
        raise TypeError('All elements in the iterable must be floats')
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0.0
    mean = total / count
    if abs(mean * count - total) > MEAN_CALCULATION_EPSILON:
        raise ValueError('Floating-point precision error in mean calculation')
    return mean
if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    print(calculate_mean(sample_values))