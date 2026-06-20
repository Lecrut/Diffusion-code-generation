class ArithmeticOperations:
    def add(self, x: int, y: int) -> int:
        return x + y
    
    def subtract(self, x: int, y: int) -> int:
        return x - y

if __name__ == '__main__':
    calc = ArithmeticOperations()
    print(calc.add(15, 7))
    print(calc.subtract(23, 4))