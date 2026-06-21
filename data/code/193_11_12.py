def list_sum(iterable: list[int]) -> int:
    return sum(iterable)

class SumCalculator:
    @staticmethod
    def calculate_sum(numbers: list[int]) -> int:
        return list_sum(numbers)

if __name__ == '__main__':
    calculator = SumCalculator()
    print(f"Sum of [1, 2, 3, 4, 5]: {calculator.calculate_sum([1, 2, 3, 4, 5])}")
    print(f"Sum of [10, -5, 20, 0]: {calculator.calculate_sum([10, -5, 20, 0])}")
    print(f"Sum of []: {calculator.calculate_sum([])}")
    print(f"Sum of [100]: {calculator.calculate_sum([100])}")