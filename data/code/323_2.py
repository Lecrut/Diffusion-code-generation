class NumberOperations:
    def subtract(self, a, b):
        return a - b
if __name__ == '__main__':
    calculator = NumberOperations()
    result1 = calculator.subtract(10, 4)
    print(f"10 - 4 = {result1}")
    result2 = calculator.subtract(50, 25)
    print(f"50 - 25 = {result2}")