import statistics

def compute_mean(numbers):
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
    print(compute_mean(sample_numbers))