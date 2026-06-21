class Statistics:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def calculate_mean(numbers):
        if not numbers:
            return 0.0
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    stats = Statistics(sample_values)
    mean_value = stats.calculate_mean(stats.data)
    print(f"Mean of {sample_values}: {mean_value}")