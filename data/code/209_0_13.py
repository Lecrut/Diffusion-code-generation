import statistics

def calculate_average(numbers):
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_numbers = [15, 25, 35, 45, 55]
    average_result = calculate_average(sample_numbers)
    print(average_result)