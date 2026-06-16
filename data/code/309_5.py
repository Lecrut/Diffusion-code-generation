class ListCalculator:
    def __init__(self, numbers: list[int | float]):
        self._numbers: list[int | float] = numbers
    def calculate_sum(self) -> int | float:
        total_sum: int | float = 0
        for number in self._numbers:
            total_sum += number
        return total_sum
if __name__ == '__main__':
    sample_data: list[int | float] = [1, 5.5, 10, -3.2]
    calculator = ListCalculator(sample_data)
    result: int | float = calculator.calculate_sum()
    print(result)