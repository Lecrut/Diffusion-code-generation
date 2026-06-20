class ArithmeticOperations:
    def subtract(self, a, b):
        return a - b

if __name__ == '__main__':
    ops = ArithmeticOperations()
    result1 = ops.subtract(10.5, 4.2)
    result2 = ops.subtract(3.7, 1.8)
    print(f"Result 1: {result1}")
    print(f"Result 2: {result2}")