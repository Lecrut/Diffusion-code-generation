class MathOperations:
    @staticmethod
    def calculate_sum(a: int, b: int) -> int:
        return a + b
    
    @staticmethod
    def calculate_difference(a: int, b: int) -> int:
        return a - b

if __name__ == '__main__':
    num1 = 20
    num2 = 8
    sum_result = MathOperations.calculate_sum(num1, num2)
    diff_result = MathOperations.calculate_difference(num1, num2)
    print((sum_result, diff_result))