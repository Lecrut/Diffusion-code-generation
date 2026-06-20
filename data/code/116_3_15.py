class SumCalculator:
    A = 10
    B = 20
    C = 30
    
    @staticmethod
    def add_three(a, b, c):
        return a + b + c
    
if __name__ == '__main__':
    calculator = SumCalculator()
    result = SumCalculator.add_three(SumCalculator.A, SumCalculator.B, SumCalculator.C)
    print(result)