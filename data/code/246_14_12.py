class ArithmeticOperations:
    def add(self, x: int, y: int) -> int:
        return x + y

if __name__ == '__main__':
    calc = ArithmeticOperations()
    result1 = calc.add(5, 3)
    result2 = calc.add(10, 7)
    print(result1)
    print(result2)