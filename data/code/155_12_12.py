class SumCalculator:
    @staticmethod
    def calculate_sum(numbers):
        return sum(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 35, 42]
    result = SumCalculator.calculate_sum(sample_values)
    print(f"The total sum is: {result}")