class SumCalculator:
    @staticmethod
    def calculate_sum(sequence: list[int]) -> int:
        total = 0
        for number in sequence:
            total += number
        return total

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.calculate_sum([1, 2, 3, 4, 5])
    print(result)