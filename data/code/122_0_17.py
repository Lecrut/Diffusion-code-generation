import statistics

def calculate_average(numbers):
    if not numbers:
        return None
    try:
        return statistics.mean(numbers)
    except TypeError:
        raise ValueError("All elements in the list must be numbers")

if __name__ == '__main__':
    sample_numbers = [12, 24, 36, 48, 60]
    average = calculate_average(sample_numbers)
    print(average)