import statistics

def calculate_average(numbers):
    if not numbers:
        return None
    try:
        return statistics.mean(numbers)
    except TypeError:
        raise ValueError("All elements in the list must be numbers")

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    average = calculate_average(sample_values)
    print(average)