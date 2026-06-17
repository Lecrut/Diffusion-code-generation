class NumberOperations:
    def subtract(self, a, b):
        return a - b
if __name__ == '__main__':
    calculator = NumberOperations()
    result1 = calculator.subtract(10, 5)
    print(f"10 - 5 = {result1}")
    result2 = calculator.subtract(25, 12)
    print(f"25 - 12 = {result2}")