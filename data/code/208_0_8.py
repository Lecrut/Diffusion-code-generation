import statistics

MEAN_CALCULATION_THRESHOLD = 10**-8

def calculate_mean(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    if abs(mean - round(mean, 8)) < MEAN_CALCULATION_THRESHOLD:
        return round(mean, 8)
    return mean

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 6.7, 5.0]
    print(calculate_mean(sample_values))