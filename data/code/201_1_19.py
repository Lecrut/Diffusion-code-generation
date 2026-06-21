import statistics

def calculate_average(numbers):
    if not numbers:
        return 0
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(f"Average of {sample_numbers}: {calculate_average(sample_numbers)}")