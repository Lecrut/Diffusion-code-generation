import random

def validate_data(data):
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Data must be a non-empty list")

def find_median_efficient(data):
    validate_data(data)
    n = len(data)
    sorted_data = sorted(data)
    mid = n // 2
    if n % 2 == 1:
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0

if __name__ == '__main__':
    large_dataset = [random.randint(1, 1000000) for _ in range(1000000)]
    median_value = find_median_efficient(large_dataset)
    print(median_value)