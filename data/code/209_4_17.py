from functools import reduce

class DataProcessor:
    @staticmethod
    def sum_and_count(data):
        return reduce(lambda acc, x: (acc[0] + x, acc[1] + 1), data, (0, 0))

    @staticmethod
    def calculate_average(data):
        total, count = DataProcessor.sum_and_count(data)
        if count == 0:
            return 0
        return total / count

if __name__ == '__main__':
    sample_data = [2, 4, 6, 8, 10]
    print(f"Average of {sample_data}: {DataProcessor.calculate_average(sample_data)}")