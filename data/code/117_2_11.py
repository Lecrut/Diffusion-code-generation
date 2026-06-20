class NumberOperations:
    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

if __name__ == '__main__':
    num1 = 25.0
    num2 = 10.0
    result = NumberOperations.subtract(num1, num2)
    print(result)