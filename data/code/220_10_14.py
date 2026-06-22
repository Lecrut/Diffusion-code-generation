import statistics

def calculate_mean(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_numbers = [3.5, 2.1, 4.8, 5.0]
    try:
        mean_value = calculate_mean(sample_numbers)
        print(f"The arithmetic mean is: {mean_value}")
    except ValueError as e:
        print(e)