class SumCalculator:
    @staticmethod
    def calculate_sum(numbers: list) -> int:
        return sum(numbers)

if __name__ == '__main__':
    calculator = SumCalculator()
    sample_lists = [
        [1, 2, 3, 4, 5],
        [10, -5, 20.5, 0],
        [],
        [100]
    ]
    for lst in sample_lists:
        print(f"Sum of {lst}: {calculator.calculate_sum(lst)}")