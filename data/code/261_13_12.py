import random

class DataProcessor:
    @staticmethod
    def calculate_median(data):
        data.sort()
        n = len(data)
        mid = n // 2
        if n % 2 == 0:
            return (data[mid - 1] + data[mid]) / 2.0
        else:
            return data[mid]

if __name__ == '__main__':
    sample_data = [random.randint(1, 1000) for _ in range(100)]
    median_value = DataProcessor.calculate_median(sample_data)
    print(median_value)