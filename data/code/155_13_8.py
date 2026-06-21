class SumCalculator:
    @staticmethod
    def calculate_sum(numbers):
        return sum(numbers)

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    total = SumCalculator.calculate_sum(data)
    print("Total sum:", total)