class IntegerArithmetic:
    def __init__(self, minuend: int, subtrahend: int):
        self.minuend = minuend
        self.subtrahend = subtrahend

    def subtract(self) -> int:
        return self.minuend - self.subtrahend

if __name__ == '__main__':
    a = 1000000000
    b = 500000000
    calculator = IntegerArithmetic(a, b)
    result = calculator.subtract()
    print(result)