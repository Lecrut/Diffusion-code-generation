class SumCalculator:
    def __init__(self):
        self.total = 0

    def add(self, number: int) -> None:
        self.total += number

    def get_sum(self) -> int:
        return self.total

if __name__ == '__main__':
    calculator = SumCalculator()
    for num in [1, 2, 3, 4, 5]:
        calculator.add(num)
    print(calculator.get_sum())