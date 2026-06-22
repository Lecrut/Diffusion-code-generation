import statistics

def calculate_mean(numbers):
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_numbers = [3.5, 2.1, 4.8, 5.6, 2.9]
    print(calculate_mean(sample_numbers))