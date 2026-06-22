class ArithmeticOperations:
    def add(self, a, b):
        return a + b

if __name__ == '__main__':
    calc = ArithmeticOperations()
    result1 = calc.add(3, 5)
    print(result1)
    result2 = calc.add(-10, 20)
    print(result2)