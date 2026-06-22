class DataProcessor:
    @staticmethod
    def calculate_mean(values):
        total = sum(values)
        count = len(values)
        return total / count if count > 0 else 0

if __name__ == '__main__':
    sample_values = [5, 10, 15, 20]
    result = DataProcessor.calculate_mean(sample_values)
    print(result)