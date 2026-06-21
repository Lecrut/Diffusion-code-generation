import statistics

def calculate_mean(numbers):
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = [7.2, 5.3, 8.9, 6.4, 9.0]
    print(calculate_mean(sample_values))