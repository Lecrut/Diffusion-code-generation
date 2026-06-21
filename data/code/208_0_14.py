import statistics

MEAN_SAMPLE = [3.5, 2.1, 4.8, 6.7, 5.0]

def calculate_mean(numbers):
    return statistics.mean(numbers)

if __name__ == '__main__':
    result = calculate_mean(MEAN_SAMPLE)
    print(result)