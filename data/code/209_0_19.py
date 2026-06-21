import statistics

def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty.")
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    average = calculate_average(sample_values)
    print(average)