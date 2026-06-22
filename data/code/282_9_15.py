class SumCalculator:
    def __init__(self, sequence: list[int]):
        self.sequence = sequence

    def calculate_sum(self) -> int:
        total = 0
        for number in self.sequence:
            total += number
        return total

if __name__ == '__main__':
    calculator = SumCalculator([1, 2, 3, 4, 5])
    result = calculator.calculate_sum()
    print(result)