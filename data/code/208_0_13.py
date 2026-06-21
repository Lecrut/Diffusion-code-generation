import statistics

def calculate_mean(numbers):
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 6.7, 5.0]
    mean_value = calculate_mean(sample_values)
    print(mean_value)