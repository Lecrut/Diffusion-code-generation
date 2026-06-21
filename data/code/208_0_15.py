import statistics

def calculate_mean(numbers):
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = [2.5, 4.3, 1.8, 3.7, 5.6]
    mean_value = calculate_mean(sample_values)
    print(mean_value)