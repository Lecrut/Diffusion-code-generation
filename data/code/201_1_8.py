import statistics

def calculate_average(numbers):
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_numbers = [2, 4, 6, 8, 10]
    result = calculate_average(sample_numbers)
    print(f"Average of {sample_numbers}: {result}")