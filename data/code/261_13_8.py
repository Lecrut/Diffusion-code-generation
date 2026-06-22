import random

def validate_data(data):
    if not isinstance(data, list) or len(data) != 100:
        raise ValueError("Data must be a list of exactly 100 integers.")
    for value in data:
        if not isinstance(value, int) or value < 1 or value > 1000:
            raise ValueError("All values must be integers between 1 and 1000.")

def calculate_median(data):
    validate_data(data)
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

if __name__ == '__main__':
    sample_data = [random.randint(1, 1000) for _ in range(100)]
    median_value = calculate_median(sample_data)
    print(median_value)