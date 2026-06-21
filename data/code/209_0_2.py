import statistics

def calculate_average(numbers):
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    average = calculate_average(sample_numbers)
    print(average)