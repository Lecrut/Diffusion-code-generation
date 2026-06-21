import statistics

def calculate_average(numbers):
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    avg_result = calculate_average(sample_values)
    print(avg_result)