import random

def calculate_median(data):
    data.sort()
    n = len(data)
    mid = n // 2
    return (data[mid - 1] + data[mid]) / 2 if n % 2 == 0 else data[mid]

if __name__ == '__main__':
    sample_data = [random.randint(1, 1000) for _ in range(100)]
    median_value = calculate_median(sample_data)
    print(median_value)