import statistics

def calculate_mean(numbers):
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_numbers = [2.5, 3.0, 4.5, 6.0, 7.5]
    mean_value = calculate_mean(sample_numbers)
    print(mean_value)