class SumCalculator:
    @staticmethod
    def calculate_sum(numbers):
        if not isinstance(numbers, list) or not all(isinstance(num, int) for num in numbers):
            raise ValueError("Input must be a list of integers")
        return sum(numbers)

if __name__ == '__main__':
    calculator = SumCalculator()
    sample_numbers = [10, 25, 5, 40, 15]
    result = calculator.calculate_sum(sample_numbers)
    print(result)