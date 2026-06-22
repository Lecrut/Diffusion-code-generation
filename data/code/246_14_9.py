class SumCalculator:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    result = SumCalculator.add(5, 3)
    print(result)