class NumberOperations:
    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

if __name__ == '__main__':
    result = NumberOperations.subtract(12.5, 7.3)
    print(result)