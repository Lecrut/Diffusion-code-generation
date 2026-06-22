import random

def calculate_median(data):
    if not all(isinstance(x, int) and 1 <= x <= 1000 for x in data):
        raise ValueError("Data must contain only integers within the range of 1 to 1000.")
    data.sort()
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    else:
        return data[mid]

if __name__ == '__main__':
    sample_data = [random.randint(1, 1000) for _ in range(100)]
    try:
        median_value = calculate_median(sample_data)
        print(median_value)
    except ValueError as e:
        print(e)