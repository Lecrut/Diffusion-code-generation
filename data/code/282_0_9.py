class SumCalculator:
    @staticmethod
    def calculate_total(numbers):
        return sum(numbers)

if __name__ == '__main__':
    numbers = [10, 25, 40, 5]
    total_sum = SumCalculator.calculate_total(numbers)
    print(total_sum)