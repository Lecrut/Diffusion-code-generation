class MeanCalculator:
    @staticmethod
    def calculate_mean(numbers):
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 5.0]
    print(MeanCalculator.calculate_mean(sample_values))