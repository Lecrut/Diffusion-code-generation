import statistics

def calculate_mean(numbers):
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = [10.5, 20.3, 30.7, 40.2, 50.8]
    print(calculate_mean(sample_values))