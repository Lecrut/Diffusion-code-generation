import statistics

def calculate_average(numbers):
    if not numbers:
        return None
    try:
        avg = statistics.mean(numbers)
        return avg
    except TypeError:
        raise ValueError("All elements in the list must be numbers")

if __name__ == '__main__':
    sample_numbers = [5, 10, 15, 20, 25]
    result = calculate_average(sample_numbers)
    print(result)