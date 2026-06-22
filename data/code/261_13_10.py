import random

def calculate_median(data):
    sorted_data = sorted(data)
    length = len(sorted_data)
    middle_index = length // 2
    if length % 2 == 0:
        return (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2.0
    else:
        return sorted_data[middle_index]

if __name__ == '__main__':
    sample_data = [random.randint(1, 1000) for _ in range(100)]
    median_value = calculate_median(sample_data)
    print(median_value)