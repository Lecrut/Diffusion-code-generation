class MaxMinCalculator:
    @staticmethod
    def calculate_difference(numbers: list) -> int:
        return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [10, 4, 25, 7, 5]
    result = MaxMinCalculator.calculate_difference(sample_values)
    print(result)