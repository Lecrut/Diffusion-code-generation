import statistics

def calculate_mean(numbers):
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_numbers = [4.5, 3.2, 5.6, 7.8, 6.1]
    mean_value = calculate_mean(sample_numbers)
    print(mean_value)