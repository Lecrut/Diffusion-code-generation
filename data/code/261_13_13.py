import random

def calculate_median(data):
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