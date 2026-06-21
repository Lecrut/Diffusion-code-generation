class SumCalculator:
    def calculate_sum(self, numbers):
        return sum(numbers)

if __name__ == '__main__':
    calculator = SumCalculator()
    result1 = calculator.calculate_sum([10, 20, 35, 42])
    result2 = calculator.calculate_sum([])
    print(f"The total sum of [10, 20, 35, 42] is: {result1}")
    print(f"The total sum of an empty list is: {result2}")