import statistics

def calculate_average(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Input must be a list of numbers")
    if not numbers:
        return None
    try:
        return statistics.mean(numbers)
    except TypeError:
        raise ValueError("All elements in the list must be numbers")

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    print(calculate_average(sample_numbers))