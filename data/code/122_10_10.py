import statistics

def compute_mean(numbers):
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_numbers = [3.5, 2.1, 4.8, 6.7, 5.0]
    print(compute_mean(sample_numbers))