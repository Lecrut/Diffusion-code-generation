class Calculator:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    result = Calculator.add(3, 5)
    print(result)