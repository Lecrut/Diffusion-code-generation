import statistics

def calculate_average(numbers):
    if not numbers:
        return 0
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_numbers = [5, 15, 25, 35, 45]
    average_value = calculate_average(sample_numbers)
    print(f"Average of {sample_numbers}: {average_value}")