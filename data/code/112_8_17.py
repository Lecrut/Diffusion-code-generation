class SumHandler:
    @staticmethod
    def sum_two_numbers(a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    calculator = SumHandler()
    result = calculator.sum_two_numbers(3, 5)
    print(result)