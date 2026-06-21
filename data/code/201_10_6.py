import statistics

def calculate_average(numbers):
    if not numbers:
        return None
    try:
        mean = statistics.mean(numbers)
        return mean
    except TypeError as e:
        print(f"Invalid input: {e}")
        return None

if __name__ == '__main__':
    sample_numbers = [10, 25, 32, 48, 15]
    result = calculate_average(sample_numbers)
    print(result)