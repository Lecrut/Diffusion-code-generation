class AdditionCalculator:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    calculator = AdditionCalculator()
    result = calculator.add(5, 3)
    print(result)