class ArithmeticOperations:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

if __name__ == '__main__':
    arith = ArithmeticOperations()
    result_add = arith.add(15, 7)
    result_subtract = arith.subtract(15, 7)
    print(f"Sum: {result_add}")
    print(f"Difference: {result_subtract}")