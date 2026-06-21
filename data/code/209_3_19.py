class AverageCalculator:
    @staticmethod
    def calculate_average(numbers):
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [5, 10, 15, 20, 25]
    avg = AverageCalculator.calculate_average(sample_numbers)
    print(avg)